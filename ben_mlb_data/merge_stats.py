import csv
import re
import sys
import unicodedata
from pathlib import Path
 
FOLDER = Path(__file__).resolve().parent
SCRAPED, FINAL = FOLDER / "scraped_all.csv", FOLDER / "my_contracts.csv"
BATTING, PITCHING = FOLDER / "batting.csv", FOLDER / "pitching.csv"
 
MIN_TOTAL_M = 0  # leave out contracts worth less than this many millions of dollars (0 keeps all)
 
COLUMNS = [
    "id", "player", "pos", "age", "team_2024", "new_team",
    "contract_years", "total_value_usd_m", "aav_usd_m",
    "war_2024", "war_type", "games_2024", "pa_or_ip_2024",
    "obp_2024", "ops_2024", "hr_2024", "so_2024", "era_2024", "sv_2024",
    "source_id", "ethnicity_stated",
]
# our column: the Baseball-Reference column it comes from. hr and so mean home runs hit and strikeouts
# for batters, and home runs allowed and strikeouts for pitchers (war_type says which).
BATTER_STATS = {"obp_2024": "OBP", "ops_2024": "OPS", "hr_2024": "HR", "so_2024": "SO"}
PITCHER_STATS = {"era_2024": "ERA", "sv_2024": "SV", "hr_2024": "HR", "so_2024": "SO"}
RATE_STATS = ("OBP", "OPS", "ERA")  # cannot be added up across teams
 
# Baseball-Reference position codes: 1=P 2=C 3=1B 4=2B 5=3B 6=SS 7=LF 8=CF 9=RF D=DH H=PH R=PR
POSITIONS = {"1": "P", "2": "C", "3": "1B", "4": "2B", "5": "3B", "6": "SS",
             "7": "LF", "8": "CF", "9": "RF", "D": "DH", "H": "PH", "R": "PR"}
 
 
 
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
 
 
def read_csv(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))
 
 
def write_csv(path, fields, rows):
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields, restval="", extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
 
 
def read_export(path, kind):
    """{clean name: [rows]} for one Baseball-Reference export (kind is 'batting' or 'pitching')."""
    with open(path, newline="", encoding="utf-8-sig") as f:
        lines = list(csv.reader(f))
    start = next((i for i, line in enumerate(lines) if "Name" in line or "Player" in line), None)
    if start is None:
        sys.exit(f"{path.name}: no header row with 'Name' or 'Player'. Re-export the Baseball-Reference table.")
    header = ["Name" if c == "Player" else c for c in lines[start]]
    table = {}
    for line in lines[start + 1:]:
        row = dict(zip(header, line))
        if row.get("Name") and row["Name"] != "Name":
            row["kind"] = kind
            table.setdefault(clean(row["Name"]), []).append(row)
    return table
 
 
def team_of(row):
    return row.get("Team") or row.get("Tm") or ""
 
 
def position_of(row):
    if row["kind"] == "batting":  # the first position code Baseball-Reference lists
        letters = re.sub(r"[^0-9DHR]", "", row.get("Pos", ""))
        return POSITIONS.get(letters[:1], "")
    games, starts = num(row.get("G")), num(row.get("GS"))
    if games and starts is not None:
        return "SP" if starts * 2 >= games else "RP"
    return "P"
 
 
def to_thirds(ip):  # innings like 104.2 mean 104 and two thirds
    whole, _, part = str(ip).partition(".")
    return int(whole or 0) * 3 + int(part or 0)
 
 
def stats_for(key, batting, pitching):
    """Return (stats dict, note). The dict is None when the player cannot be matched."""
    bat, pit = batting.get(key, []), pitching.get(key, [])
    if pit:  # pitchers also appear in the batting export with 0 plate appearances; ignore those
        bat = [r for r in bat if num(r.get("PA"))]
    rows = bat + pit
    if not rows:
        return None, "no 2024 MLB row in either export"
    if bat and pit:
        return None, "found in both exports (check by hand)"
    kind = rows[0]["kind"]
    wanted = BATTER_STATS if kind == "batting" else PITCHER_STATS
    combined = [r for r in rows if re.fullmatch(r"\dTM|TOT", team_of(r))]
    if len(rows) == 1 or len(combined) == 1:
        x = rows[0] if len(rows) == 1 else combined[0]
        war, games, volume, team, note = x["WAR"], x.get("G", ""), x.get("PA" if kind == "batting" else "IP", ""), team_of(x), ""
        extra = {col: x.get(src, "") for col, src in wanted.items()}
    elif not combined:  # several team rows and no combined row: add them up
        x = rows[0]
        team = "/".join(team_of(r) for r in rows)
        war = round(sum(num(r["WAR"]) or 0 for r in rows), 1)
        games = int(sum(num(r.get("G")) or 0 for r in rows))
        if kind == "batting":
            volume = int(sum(num(r.get("PA")) or 0 for r in rows))
        else:
            thirds = sum(to_thirds(r.get("IP", "0")) for r in rows)
            volume = f"{thirds // 3}.{thirds % 3}"
        extra = {col: "" if src in RATE_STATS else int(sum(num(r.get(src)) or 0 for r in rows))
                 for col, src in wanted.items()}
        note = f"2024 stats added up across team rows ({team}); rate stats left blank"
    else:
        return None, "several combined rows (check by hand)"
    return {"pos": position_of(x), "age": x.get("Age", ""), "team": team, "war": war, "kind": kind,
            "games": games, "volume": volume, "extra": extra,
            "code": x.get("Pos", "") if kind == "batting" else ""}, note
 
 
def build():
    for path in (SCRAPED, BATTING, PITCHING):
        if not path.exists():
            sys.exit(f"{path.name} is not in the folder {FOLDER}")
    batting, pitching = read_export(BATTING, "batting"), read_export(PITCHING, "pitching")
 
    rows, seen, left_out, duplicates, below_minimum, trades = [], set(), [], [], 0, 0
    for s in read_csv(SCRAPED):
        if s["flag"] == "trade_not_a_signing":
            trades += 1
            continue
        if not (s["flag"] == "ok" or s["flag"].lower().startswith("fixed")):
            left_out.append(f"unresolved flag ({s['flag']}): {s['player'] or s['check_text_start'][:60]}")
            continue
        if clean(s["player"]) in seen:
            duplicates.append(f"{s['player']} ({s['source_id']})")
            continue
        seen.add(clean(s["player"]))
        years, total, note = num(s["years"]), num(s["total_value_usd_m"]), s["note"]
        if total is not None and total < MIN_TOTAL_M:
            below_minimum += 1
            continue
        if years is None or total is None:
            note = (note + "; " if note else "") + "years and/or value missing"
        rows.append({
            "player": s["player"], "new_team": s["team"], "contract_years": int(years) if years is not None else "",
            "total_value_usd_m": total if total is not None else "",
            "aav_usd_m": round(total / years, 2) if years and total is not None else "",
            "contract_note": note, "source_id": s["source_id"],
        })
    rows.sort(key=lambda r: -(r["total_value_usd_m"] if r["total_value_usd_m"] != "" else -1))
 
    not_filled = []
    for number, r in enumerate(rows, 1):
        r["id"] = f"FA{number:03d}"
        stats, note = stats_for(clean(r["player"]), batting, pitching)
        if stats is None:
            r["contract_note"] = (r["contract_note"] + "; " if r["contract_note"] else "") + "2024 stats not filled: " + note
            not_filled.append(f"{r['id']} {r['player']}: {note}")
            continue
        extra = [note] if note else []
        if stats["code"]:
            extra.append(f"BR position code {stats['code']}")
        if extra:
            r["contract_note"] = (r["contract_note"] + "; " if r["contract_note"] else "") + "; ".join(extra)
        r.update({"pos": stats["pos"], "age": stats["age"], "team_2024": stats["team"], "war_2024": stats["war"],
                  "war_type": stats["kind"], "games_2024": stats["games"], "pa_or_ip_2024": stats["volume"],
                  "war_source": "Baseball-Reference 2024 value " + stats["kind"], **stats["extra"]})
 
    write_csv(FINAL, COLUMNS, rows)
    print(f"wrote {len(rows)} rows to {FINAL.name}  |  2024 stats filled for {len(rows) - len(not_filled)}")
    if not_filled:
        print("no 2024 stats (players with no MLB season in 2024 are expected here):")
        for line in not_filled:
            print("  ", line)
    if below_minimum:
        print(f"left out because total value is under ${MIN_TOTAL_M}M: {below_minimum}")
    if trades:
        print(f"left out because the slide is a trade, not a signing: {trades}")
    if duplicates:
        print(f"listed in more than one source, kept once (first source wins): {len(duplicates)}")
    if left_out:
        print(f"left out {len(left_out)}:")
        for line in left_out:
            print("  ", line)
 
 
if __name__ == "__main__":
    build()
