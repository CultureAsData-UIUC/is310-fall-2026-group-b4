# MLB 2024-2025 Free-Agent Contracts Dataset
Ben Taylor

## The Dataset
The dataset describes the contracts signed by MLB free agents in the 2024-2025 offseason, plus each player's 2024 season statistics and a hand-compiled nationality field. It contains 55 rows, one per signing. It combines two sources:

- **Bleacher Report Free-Agent Tracker** This article supplied the list of players and the teams they signed with, alongside the contract length and value.
- **Baseball-Reference Database** This database provided the 2024 batting and pitching statistics through an export that supplied the players statistics.

Through this dataset, I aim to answer my larger question on 'How baseball contract data can be used to study racial inequality.' The dataset I created was inspired by a dataset created by Masella (2017), who created his own datasets from the years 2012-2015 tracking MLB players contracts and their statistics in according years. I used his datasets as a model for what my contract dataset might contain, but did not reuse his data. I built a new, smaller dataset for a specific year. 

For the initial dataset, I focused on just one specific MLB offseason, as to keep my scope narrow. The biggest challenge I've faced while creating the initial dataset was how to represent a players race. I am still working on a solution to this without inferring, but for now have settled on a nationality column that tracks a players nationality, rather than their race.

## Approach
I built this dataset from scratch while also auditing some data as well.

- **Scratch:** From scratch, I created the 55 rows, scraping data from the Bleacher Report article to create an individual row for each free agent signing. I then conducted my own research to fill in certain missing values, and most importantly filled in the nationality field on my own. 
- **Audit:** I exported two datasets from Baseball Reference, 'batting.csv' and 'pitching.csv', and then merged them into my created dataset. 

## How The Dataset Was Built

To create this dataset, I uwed two different webscrapers. The first one was **scrape_contracts.py**. This scraper was built in accordance to Bleacher Reports robots.txt. The scraper read the article's 74 slides, and pulled out players, teams, years, contract length, and contract value. It then wrote that into **scraped_all.csv**.

This scraper was extremely beneficial as it helped expedite the dataset creation, so I didn't have to go through all 74 articles slides myself. 

This scraper is limited as it did not obtain all the data accurately and I had to double check a few of it's inputs. 

I also used a merger, **merge_stats.py**. This merger joined the **scraped_all.csv** with the **batting.csv** and **pitching.csv** exports from Baseball Reference by player name. It then created **contracts.csv** which was my final dataset, combining players, signing details, and their performance.

This merger was limited as players who aren't the only player with their name were found in both exports and their data was not copied over. This needed to be fixed by hand.

## Dataset Columns

The dataset contains 55 rows and 21 columns.

1. id (Identifier)
2. player (players name)
3. pos (position)
4. age (years)
5. team_2024 (previous team)
6. new_team (new team)
7. contract_years (length of contract)
8. total_value_usd_m (value of contract in millions)
9. aav_usd_m (average annual value of contract)
10. war_2024 (wins above replacement)
11. war_type (identifies if player is batter or pitcher)
12. games_2024 (games played)
13. pa_or_ip_2024 (plate apperances or innings pitched)
14. obp_2024 (on base percentage)
15. ops_2024 (on base plus slugging)
16. era_2024 (earned run average)
17. sv_2024 (saves)
18. hr_2024 (home runs)
19. so_2024 (strike outs)
20. source_id (Bleacher or hand)
21. nationality (players nationality)

There are some blank values coming from players who did not play in the 2024 season. Also blank values for batting statistics by pitchers, and vise versa.

## Decisions

The biggest challenge I faced when creating this dataset was determining how to identify a players demographic. Initially, I wanted to investigate salary contracts when compared to race, however, there is no clear data listed anywhere on players race. I did not want to infer race either, so I decided to move on from that (for now), until I could come up with a solution. To replace this, I decided to focus on nationality, which isn't perfect. It does not represent race at all, and rather would create a whole new way of looking at salary contracts in comparison to nationality. 

I also need to decide how to bridge the gap between statistics differences between batters and pitchers. WAR is the only stat that they share in common currently. 

I made the decision as well, to exclude 18 pages from the Bleacher Report article that was scraped. These players were involved in trades, not free agent signings, so I decided to drop them as they were not signing a new contract. 

## Limitations

One limitation in my dataset is the inability to represent the extra details of contracts such as opt-outs, deferrals, and bonuses. 

Another large limitation is the nationality column, which doesn't represent much besides a players country of origin.

# Next Steps

I plan on pursuing (Option 1) by creating more data computationally. My scrapers worked pretty well when creating this dataset, and I hope to create more scrapers as well as find more resources with contract data on more years. This should help expand my dataset to 500-1000+ items. 

I will first find sources that have free agent signings from my desired years, to test if they can be scraped. I will also continue to search for any resource that tracks MLB players race in anyway. I also am considering reaching out to Masella, and asking him how he identified players race. 

Overall, my main goal before scraping the rest of the contracts, is to find a better way to represent a players race. Currently I have no answers without inferring, so I will continue to search and see if it is possible to identify a players race from any source.

## References

- Masella, John. 2017. Racial Salary Discrimination in Major League Baseball: A Closer Look. Haverford College. Haverford Dataverse. https://doi.org/10.7910/DVN/ZUMXXL

- Bureau of Labor Statistics / Census Bureau, Current Population Survey race and ethnicity methodology (https://www.bls.gov/cps/rvcps03.pdf).

