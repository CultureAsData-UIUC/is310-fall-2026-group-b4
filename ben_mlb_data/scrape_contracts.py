import csv
import re
import sys
import time
import unicodedata
from pathlib import Path
from urllib.parse import urlparse
from urllib.robotparser import RobotFileParser
 
import requests
from bs4 import BeautifulSoup
 
FOLDER = Path(__file__).resolve().parent
RAW = FOLDER / "raw_html"
SCRAPED = FOLDER / "scraped_all.csv"
 
USER_AGENT = "course-project-scraper"  # a plain, honest name for what this is
HEADERS = {"User-Agent": USER_AGENT}
 
SOURCES = [
    # parser "slides": the Bleacher Report article is a slideshow, one signing or trade per slide.
    {"id": "BLEACHER", "name": "bleacher", "parser": "slides",
     "url": "https://bleacherreport.com/articles/10145364-mlb-free-agent-tracker-2024-updates-on-all-the-latest-contract-signings-and-trades"},
    # Optional extra sources for cross-checking. Remove the # to use them.
    # {"id": "ABC7", "name": "abc7", "min_chars": 90, "tags": ["p"],
    #  "url": "https://abc7news.com/post/mlb-free-agency-tracker-latest-2024-25-offseason-trades-moves/15493386/"},
    # {"id": "NBCSD", "name": "nbcsd", "min_chars": 25, "tags": ["p", "li"],
    #  "url": "https://www.nbcsandiego.com/mlb/mlb-opening-day-2025-heres-everything-you-missed-during-the-offseason/3788195/"},
]
INCLUDE_TRADES = False  # the article's 74 slides include 18 trades; True marks them "ok" so step 2 keeps them (no contract)
SCRAPED_FIELDS = ["source_id", "source_url", "player", "team", "years", "total_value_usd_m",
                  "note", "flag", "check_text_start", "status"]
 
NICKNAMES = {
    "Diamondbacks": "Arizona Diamondbacks", "Athletics": "Athletics", "Braves": "Atlanta Braves",
    "Orioles": "Baltimore Orioles", "Red Sox": "Boston Red Sox", "Cubs": "Chicago Cubs",
    "White Sox": "Chicago White Sox", "Reds": "Cincinnati Reds", "Guardians": "Cleveland Guardians",
    "Rockies": "Colorado Rockies", "Tigers": "Detroit Tigers", "Astros": "Houston Astros",
    "Royals": "Kansas City Royals", "Angels": "Los Angeles Angels", "Dodgers": "Los Angeles Dodgers",
    "Marlins": "Miami Marlins", "Brewers": "Milwaukee Brewers", "Twins": "Minnesota Twins",
    "Mets": "New York Mets", "Yankees": "New York Yankees", "Phillies": "Philadelphia Phillies",
    "Pirates": "Pittsburgh Pirates", "Padres": "San Diego Padres", "Giants": "San Francisco Giants",
    "Mariners": "Seattle Mariners", "Cardinals": "St. Louis Cardinals", "Rays": "Tampa Bay Rays",
    "Rangers": "Texas Rangers", "Blue Jays": "Toronto Blue Jays", "Nationals": "Washington Nationals",
}
NUMBER_WORDS = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7,
                "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12, "fifteen": 15}
YEARS = re.compile(r"\b(\d+|" + "|".join(NUMBER_WORDS) + r")[- ]year", re.I)
DOLLARS = re.compile(r"\$\s?([\d.,]+)\s?(?:million|M)\b", re.I)
NOT_NAMES = {"story", "grade", "grades"}
ROLE = r"(?i:outfielder|infielder|first baseman|second baseman|third baseman|shortstop|catcher|designated hitter|left-hander|right-hander|lefty|righty|reliever|pitcher|slugger|free agent|free-agent)"
NAME = r"[A-Z][\w.'’-]*(?:\s+[A-Z][\w.'’-]*){1,2}"
AFTER_ROLE = re.compile(ROLE + r"\s+(" + NAME + r")")
POS_LEAD = re.compile(r"^\W*(?:\d{1,2}[.)]\s*)?(1B|2B|3B|SS|OF|LF|CF|RF|DH|SP|RP|C|P|B)\s+(" + NAME + r")\s*,")
STARTS_WITH_NAME = re.compile(r"^\W*(" + NAME + r")\s+(?:and|agreed|agrees|signed|re-signed|is|are|has|have|will)\b")
LEADING = re.compile(r"^\W*\d{0,2}[.)]?\s*(" + NAME + r")\s*[,:–—-]")
 
 
# ---------- helpers ----------
 
def clean(name):
    """'Gary Sánchez*' and 'Gary Sanchez' count as the same player."""
    name = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode()
    return " ".join(re.sub(r"[^a-z ]", "", name.lower()).split())
 
 
def num(text):
    try:
        return float(str(text).replace(",", ""))
    except ValueError:
        return None
 
 
def write_csv(path, fields, rows):
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields, restval="", extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
 
 
def teams_in(text, ignore_case=False):
    """Full names of the teams mentioned in the text, in the order they appear."""
    found = []
    for nickname, full in NICKNAMES.items():
        match = re.search(rf"\b{re.escape(nickname)}\b", text, re.I if ignore_case else 0)
        if match and full not in [f for _, f in found]:
            found.append((match.start(), full))
    return [full for _, full in sorted(found)]
 
 
def robots_allows(url):
    """Read robots.txt with our own user agent. Returns (allowed, reason)."""
    parts = urlparse(url)
    try:
        response = requests.get(f"{parts.scheme}://{parts.netloc}/robots.txt", headers=HEADERS, timeout=30)
    except requests.RequestException as error:
        return False, f"could not read robots.txt ({error})"
    if response.status_code == 404:
        return True, "the site has no robots.txt"
    if response.status_code != 200:
        return False, f"robots.txt returned HTTP {response.status_code}, so the rules are unknown"
    rules = RobotFileParser()
    rules.parse(response.text.splitlines())
    if rules.can_fetch(USER_AGENT, url):
        return True, "robots.txt allows it"
    return False, "robots.txt disallows this page"
 
 
def get_page(source, refresh):
    """HTML from the saved copy, or one polite download. None means skipped."""
    RAW.mkdir(exist_ok=True)
    path = RAW / f"{source['name']}.html"
    if path.exists() and not refresh:
        print(f"{source['id']}: using the saved copy {path}")
        return path.read_text(encoding="utf-8")
    allowed, reason = robots_allows(source["url"])
    if not allowed:
        print(f"{source['id']}: SKIPPED. {reason}. Do not scrape it; add its rows by hand.")
        return None
    time.sleep(source.get("delay", 3))  # seconds; set "delay" on a source if its robots.txt asks for more
    response = requests.get(source["url"], headers=HEADERS, timeout=30)
    if response.status_code != 200:
        print(f"{source['id']}: SKIPPED. HTTP {response.status_code} (403 or 429 means the site is refusing or limiting you).")
        return None
    path.write_text(response.text, encoding="utf-8")
    print(f"{source['id']}: downloaded and saved to {path}")
    return response.text
 
 
def guess_name(text):
    for pattern in (AFTER_ROLE, LEADING, STARTS_WITH_NAME):
        match = pattern.search(text)
        if match and not teams_in(match.group(1)):  # "The Mets" is a team, not a player
            return match.group(1).strip()
    return ""
 
 
def parse_text(soup, source):
    """One signing per paragraph or list item."""
    rows, dropped, heading = [], [], ""
    for tag in soup.find_all(source["tags"] + ["h2", "h3", "h4"]):
        text = tag.get_text(" ", strip=True)
        if tag.name in ("h2", "h3", "h4"):
            heading = text  # a signing's name is sometimes only in the heading above it
            continue
        if "$" not in text:
            continue
        if not YEARS.search(text) or len(text) < source["min_chars"]:
            dropped.append(text)
            continue
        flags, note = [], []
        years_word = YEARS.search(text).group(1).lower()
        years = int(years_word) if years_word.isdigit() else NUMBER_WORDS[years_word]
        money = DOLLARS.search(text)  # the first dollar amount is the total value
        value = num(money.group(1)) if money else None
        if value is None:
            flags.append("value_not_found")
        teams = teams_in(text)
        if len(teams) != 1:
            flags.append(f"teams_found_{len(teams)}")
        links = [a.get_text(" ", strip=True) for a in tag.find_all("a")]
        names = [x for x in links if x.lower() not in NOT_NAMES and len(x.split()) >= 2 and not teams_in(x)]
        player = names[0] if names else ""
        lead = POS_LEAD.match(text)
        if lead and not player:  # NBC style: "OF Juan Soto, New York Mets: 15 years, $765 million"
            player = lead.group(2).strip()
            note.append(f"source lists position {lead.group(1)}")
        if not player:
            player = guess_name(text)
            flags.append("name_from_text_check" if player else "no_name_found")
        if not player:
            match = re.match(NAME, heading)
            if match and not teams_in(match.group()):
                player = match.group()
                flags[-1] = "name_from_heading_check"
        low = text.lower()
        if "opt-out" in low:
            note.append("opt-out mentioned")
        if "physical" in low:
            note.append("pending physical")
        if "finalizing" in low:
            note.append("finalizing, not yet agreed")
        if "traded" in low:
            flags.append("mentions_trade_check_row")
        rows.append({"player": player, "team": " / ".join(teams), "years": years,
                     "total_value_usd_m": "" if value is None else value, "note": "; ".join(note),
                     "flag": "; ".join(flags) or "ok", "check_text_start": text[:120]})
    return rows, dropped
 
 
TRADE = re.compile(r"\b(Traded|Trade|Acquires?|Acquired)\b", re.I)
 
 
def name_from_title(title):
    """'Alex Bregman Signs with Red Sox' -> 'Alex Bregman'; 'Andrew McCutchen, Pirates Agree...' -> 'Andrew McCutchen'."""
    for pattern in (r"^(.+?)(?:,.*?)?\s+(?:Re-?signs?|Signs?|Agrees?|Agree)\b",
                    r"^(.+?)\s+(?:Reportedly\s+)?Traded\b", r"\bAcquire\s+(.+?)\s+from\b"):
        match = re.search(pattern, title, re.I)
        if match:
            return match.group(1).strip()
    return ""
 
 
def parse_slides(soup, source):
    """One row per slide. Slide parts have ids like id/article/slide/<number>/title, /subtitle, /element/0."""
    bodies = {}
    for el in soup.find_all(id=re.compile(r"^id/article/slide/\d+/element/\d+$")):
        bodies.setdefault(el["id"].split("/")[3], []).append(el.get_text(" ", strip=True))
    rows = []
    for tag in soup.find_all(id=re.compile(r"^id/article/slide/\d+/title$")):
        sid = tag["id"].split("/")[3]
        title = tag.get_text(" ", strip=True)
        subtitle = soup.find(id=f"id/article/slide/{sid}/subtitle")
        slide = subtitle.get_text(" ", strip=True) if subtitle else ""
        body = " ".join(bodies.get(sid, [])).split("TOP NEWS")[0]  # "TOP NEWS" starts an unrelated widget
        is_trade = bool(TRADE.search(title))
        flags, note = [], [f"slide {slide}"] if slide else []
 
        years = value = ""
        money = DOLLARS.search(body)
        if money and not is_trade:
            value = num(money.group(1))
            value = "" if value is None else value
            near = body[max(0, money.start() - 60):money.end() + 60]  # years only if stated next to the dollars
            found = YEARS.search(near)
            if found:
                word = found.group(1).lower()
                years = int(word) if word.isdigit() else NUMBER_WORDS[word]
        if not is_trade:
            if years == "" and value == "":
                note.append("contract terms not stated in the slide")
            elif years == "":
                note.append("years not stated in the slide")
            elif value == "":
                note.append("value not stated in the slide")
 
        teams = teams_in(title.replace("A's", "Athletics").replace("A\u2019s", "Athletics"), ignore_case=True)
        if not teams and not is_trade:
            teams = teams_in(body)
        team = teams[0] if teams else ""
        if not is_trade and len(teams) != 1:
            flags.append(f"teams_found_{len(teams)}")
        player = name_from_title(title)
        if not player:
            flags.append("no_name_found")
        status = ""
        if is_trade:
            note.append("trade, not a free-agent contract")
            if INCLUDE_TRADES:
                status = "Traded"
            else:
                flags.append("trade_not_a_signing")
        if "extension" in title.lower():
            note.append("extension")
        if "minor-league" in title.lower():
            note.append("minor-league contract")
        low = body.lower()
        if "opt-out" in low:
            note.append("opt-out mentioned")
        if "club option" in low:
            note.append("club option mentioned")
        rows.append({"player": player, "team": team, "years": years, "total_value_usd_m": value,
                     "note": "; ".join(note), "flag": "; ".join(flags) or "ok", "status": status,
                     "check_text_start": f"{title} | {body}"[:120]})
    return rows, []
 
 
def compare_sources(all_rows):
    """Where two sources list the same player: a figure only one source states is filled in
    from the other (with a note); two different figures hold both rows back for you to check."""
    by_player = {}
    for r in all_rows:
        if r["player"]:
            by_player.setdefault(clean(r["player"]), []).append(r)
    both = agree = 0
    for rows in by_player.values():
        first = rows[0]
        for other in rows[1:]:
            if other["source_id"] == first["source_id"] or first["flag"] == "trade_not_a_signing":
                continue
            both += 1
            clash = [name for name, x, y in (("years", first["years"], other["years"]),
                                             ("value", first["total_value_usd_m"], other["total_value_usd_m"]))
                     if x != "" and y != "" and abs(float(x) - float(y)) > 0.001]
            if clash:
                print(f"  SOURCES DISAGREE: {first['player']} | {first['source_id']}: {first['years']} yrs "
                      f"${first['total_value_usd_m']}M | {other['source_id']}: {other['years']} yrs ${other['total_value_usd_m']}M")
                for row in (first, other):  # both rows are held back until you check the live pages
                    row["flag"] = "sources_disagree" if row["flag"] == "ok" else row["flag"] + "; sources_disagree"
                continue
            agree += 1
            if other["flag"] == "ok":  # fill a figure the first source did not state
                for field, label in (("years", "years"), ("total_value_usd_m", "value")):
                    if first[field] == "" and other[field] != "":
                        first[field] = other[field]
                        first["note"] = (first["note"] + "; " if first["note"] else "") + f"{label} taken from {other['source_id']}"
    print(f"players found in more than one source: {both}  |  agree or filled in: {agree}  |  disagree: {both - agree}")
 
 
def scrape(args):
    if SCRAPED.exists() and "--overwrite" not in args:
        sys.exit(f"{SCRAPED.name} already exists and may hold your hand fixes, so nothing was changed.\n"
                 f"To start over, run:  python3 scrape_contracts.py --overwrite")
    all_rows = []
    for source in SOURCES:
        html = get_page(source, "--refresh" in args)
        if html is None:
            continue
        soup = BeautifulSoup(html, "lxml")
        rows, dropped = (parse_slides if source.get("parser") == "slides" else parse_text)(soup, source)
        for r in rows:
            r["source_id"], r["source_url"] = source["id"], source["url"]
        ok = sum(1 for r in rows if r["flag"] == "ok")
        print(f"{source['id']}: rows: {len(rows)}  |  ok: {ok}  |  need checking: {len(rows) - ok}"
              f"  |  dropped paragraphs with a $: {len(dropped)}")
        for r in rows:
            if r["flag"] != "ok":
                print("  CHECK:", r["player"] or "(no name)", "|", r["flag"], "|", r["check_text_start"][:70])
        for text in dropped[:12]:
            print("  DROPPED:", text[:100])
        all_rows += rows
    if not all_rows:
        sys.exit("No rows found. Nothing was written.")
    print()
    compare_sources(all_rows)
    write_csv(SCRAPED, SCRAPED_FIELDS, all_rows)
    print(f"\nwrote {len(all_rows)} rows to {SCRAPED.name}")
 
 
if __name__ == "__main__":
    scrape(sys.argv[1:])
