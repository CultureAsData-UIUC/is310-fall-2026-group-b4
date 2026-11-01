import csv
from rich.console import Console
import pandas as pd
import cpi 

cpi.update()

# i want to be able to take in a csv file, and then adjust the salaries in it for inflation in a new column.
# i want to inflate the salaries to 2020 dollars.
df = pd.read_csv("eric_game_data/epic_games.csv")
for index, row in df.iterrows():
    salary = row["Salary"]
    year = row["Year"]
    adjusted_salary = cpi.inflate(salary, year, to=2020)
    df.at[index, "Adjusted Salary"] = adjusted_salary

df.to_csv("eric_game_data/epic_games_adjusted.csv", index=False)

