# lets do this thing
import requests
from bs4 import BeautifulSoup
import csv
import time
from rich.console import Console

console = Console()

BASE_URL = "https://h1bdata.info/index.php"
HEADERS = {"User-Agent": "is310-course-scraper/1.0 (student project; ecampos3@illinois.edu)"}
REQUEST_DELAY = 0.5  

# fine i'll make functions. i should have done this sooner
def fetch_soup(url):
    if not url:
        console.print("[red] give up bro. no link found")
        return None
    response = requests.get(f"{url}", headers = HEADERS, timeout=30)
    time.sleep(REQUEST_DELAY)
    if response.status_code != 200:
        console.print("[red] yeah not working bub. couldn't download.")
        return None
    console.print("[green] yeah we got it bub")
    return BeautifulSoup(response.text, "html.parser")

# takes in the url, provided it has a table to scrape, and the company name. 
# company name is used for logic that separates rows.
# note: when scraping, we do not capture the company. It is assumed that you will send the data to a company.csv
def scrape_table(url, company):
    console.print(f"[blue]Now scraping the Epic Games table...")
    response3 = requests.get(f"{url}", headers = HEADERS, timeout=30)
    time.sleep(REQUEST_DELAY)
    table_rows = []
    temp_row = []
    if(response3.status_code == 200):
        soup = BeautifulSoup(response3.text, "html.parser")
        table = soup.find_all(["td", "th"]) # <-- we are gonna get rows of the table. 
        
        # we are going to make a list of lists.
        # a list = [employer, job title, base salary, location, submit date, start date.]
        # a list is an item in the larger list we return.
        for element in table[5:]:
            item = element.get_text()
            console.print(f"[yellow]Found: {item}")
            if item == company:
                console.print(f"[green]ADDED {temp_row} BECAUSE {item} = {company}")
                table_rows.append(temp_row)
                temp_row = []
                console.print(f"[red]CLEARED")
                continue
            else:
                temp_row.append(item)
            
            time.sleep(REQUEST_DELAY)

    # this final check adds the last row of data that went unadded
    if not temp_row:
        pass
    else:
        console.print(f"[green]ADDED {temp_row} BECAUSE {item} = {company}")
        table_rows.append(temp_row)
        time.sleep(REQUEST_DELAY)

    return table_rows

# unnecessary, but a function that removes the first item in the list. 
# added because scrape_table has a useless first item in the list. 
def clean_data(list):
    list.pop(0)

    return list

# this will return 4 lists. job_title, salary, location, starting date
def separate_columns(list):
    job_titles = divide_data(list, 0)
    salaries = divide_data(list, 1)
    locations = divide_data(list, 2)
    starting_dates = divide_data(list, 3)
    
    return job_titles, salaries, locations, starting_dates
    

# takes a list of lists. separates the data in each individual list. 
def divide_data(list, choice):
    return_list = []
    for element in list:
        item = element[choice]
        return_list.append(item)
    return return_list

def main():

    tempList = scrape_table("https://h1bdata.info/index.php?em=+rockstar+games&job=&city=&year=all+years", "ROCKSTAR GAMES INC")
    print(tempList)
    tempList = clean_data(tempList)

    job_list, salary_list, location_list, start_date_list = separate_columns(tempList)

    print(job_list)
    print(salary_list)
    print(location_list)
    print(start_date_list)

    complete_epic_table = []
    
    for job, salary, local, date in zip(
        job_list,
        salary_list,
        location_list,
        start_date_list
    ):
        complete_epic_table.append(
            {
                "Job Title": job,
                "Salary": salary,
                "Location": local,
                "Starting Date": date
            }
        )

    fieldNames = ["Job Title", "Salary", "Location", "Starting Date"]
    with open("RockstarGames.csv", mode="w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldNames)
        writer.writeheader()
        writer.writerows(complete_epic_table)
    


main()