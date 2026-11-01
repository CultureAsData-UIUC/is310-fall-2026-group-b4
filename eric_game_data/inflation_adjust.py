import csv
from rich.console import Console
import pandas as pd
import cpi 

# takes in a dataframe. 
# 1. removes rows that are in the year 2026. The CPI calc does not have that data yet
# 2. we add an adjusted salary. row year --> 2020 dollars.
# 3. the calc returns a float. we turn round to nearest dollar and back into an int
# 4. we create an adjusted csv 
def clean_data(dataframe, company):
    df = dataframe
    df = df[df['Year'] < 2026]
    df['Adjusted Salary (2020 USD)'] = df.apply(lambda row: cpi.inflate(row['Salary'], int(row['Year']), to=2020), axis=1)
    df['Adjusted Salary (2020 USD)'] = df['Adjusted Salary (2020 USD)'].round().astype(int)
    df.to_csv(f"eric_game_data/{company}_adjusted.csv", index=False)

    return None


def main():
    cpi.update()
    # i want to be able to take in a csv file, and then adjust the salaries in it for inflation in a new column.
    # i want to inflate the salaries to 2020 dollars.
    rockstar = pd.read_csv("eric_game_data/RockstarGames.csv", encoding='cp1252')
    epic = pd.read_csv("eric_game_data/EpicGames.csv", encoding='cp1252')
    clean_data(rockstar, "RockstarGames")
    clean_data(epic, "EpicGames")


main()