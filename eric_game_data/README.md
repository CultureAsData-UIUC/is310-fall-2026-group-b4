# The Dataset 
This dataset (**combined_manipulated_data.csv**) is a collection of job listings within the video game industry. This data comes from the [H1B Salary Database](https://h1bdata.info/index.php). The database indexes Labor Condition Applications. These applications are necessary if a company wants to hire a foreigner for a position. The fortunate part of these applications are that they must share a planned starting salary. A lot of listings from companies do not list there salaries. 

From this database, I narrowed my search to two American video game companies, *Epic Games Inc* and *Rockstar Games Inc*. These two companies are large in the industry and had many positions avaiable to pull from. 

From the H1B Salary Database, I webscraped job listings from Epic and Rockstar to create preliminary datasets to start refining. 

# Road To The Dataset
The preliminary datasets, **EpicGames.csv** and **RockstarGames.csv**, collected four categories of data.
1. Job Title
2. Salary (USD)
3. Location (Job Site)
4. Starting Date (xx/xx/xxxx)

This data was a good starting point. With over 250 rows of data, this data went through another transformation where I separated the starting date and added the year. This was necessary so I could programmatically inflate/deflate the salaries to a common year. I landed on the year 2020 as my marker year. This resulted in **RockstarGames_adjusted.csv** and **EpicGames_adjusted.csv**. From these two datasets, I narrowed my search even further. 

Before the final dataset, I added another column to the data where I generalized the Job Title to a Job Category. The dataset I plan to audit also had a generalized job category. I decided this was the best course of action because a generalized job category would make comparing to similar job titles more feasible in a program. I also removed listings that had no easily catergorizable job titles. From over 250 job listings, I reduced to around 150 job listings. This resulted in the datasets, **EpicGames_manipulated.csv** and **RockstarGames_manipulated.csv**. This 



# Final Dataset
The final dataset, **combined_manipulated_data.csv**, was reduced to 100 job listings. These job listings were picked in preparation of comparing to the other dataset. I picked job listings that showed up many times in the to be audited dataset and jobs that seemed to have many occurences of different genders. The final dataset collected 8 fields of interest.

1. Job Title
2. Salary (USD)
3. Location (Job Site)
4. Starting Date (xx/xx/xxxx)
5. Year
6. Adjusted Salary (2020 USD)
7. Job Category 
8. Company

# The Dataset To Be Audited
The dataset to be audited comes from Evva Karr. She is the founder of GLITCH, a company dedicated to supporting startup game studios. Karr is a [veteran of the games industry](https://bizcommunity.gamescom.global/event/gamescom-asia-x-thailand-game-show-2026-1/person/RXZlbnRQZW9wbGVfNDg3ODIzMzc=), with fifteen years under her belt across a myriad of studios.  Between 2020 and 2021, she held an anonymous survey where game developers could report their salaries. Across two years, the dataset has collected around 900 rows of data from developers all over the world. The data is accessible from a [Google Spreadsheet](https://docs.google.com/spreadsheets/d/1cM3_iBGF8IXZfLS5GKvC0-JWh0tS6TVYJJ-HxlguinA/htmlview#?usp=sharing&pru=AAABcrSmbYk*J5OhG3eCmEl1Xu_Y325bRg). 

With this data, I seek to investigate wage discrimination in the video game industry. Karr's dataset has job titles, job categories, salaries, and self-reported genders. With my collection of job listings/salaries, I plan to see if women are being paid less than men in their respective job category/field. The audited data will provide an average for what a person can expect to be paid in a job category. I can see how close or far they are from my collection of job listings for similar job categories. 

# Why Investigate?
The discussion of wage discrimination is not new. There are many social factors that affect wages and social mobility. Men (primarily White men) are the majority of workers in video game development(Buck, 2022). This seems to be seen in Karr's dataset where, around 60% are male and 33% are female. 

Alison R. Buck, investigated some features of video game development that may result in largely male development teams. Buck examines the idea of identity wages. These "wages" represent the wages that one is paid in the form of being surrounded by people like you. Video game development is prone to crunch work, unpaid overtime, and many other challenges. Many developers go underpaid, women even more-so because there of a atmosphere of "masculine camaraderie"(Buck, 2022). 

This is seen across the industry. In the company, Riot Games, they have quite a large female portion making up their staff, hovering around 20%. Despite this, many women have given interviews citing a "sexist 'bro culture'"(Bailey, 2019). In fact, across Riot's top management of 23 people, 21 are men. 

Eric N. Bailey, in an investigation of gender composition in game development, notes that at Rockstar North, "the UK’s Gender Pay Gap database revealed that women working there earn a mean of 36% that of men". Bailey explains at the same time that this statistic does not show that women are making less for the same position(Bailey, 2022). 

Survey data in regards to wage discrimination is not new or novel, but finding data in regards to their job categories can empower people to advocate for oneself. While this investigation seeks to find wage discrimination in the games industry, it is ultimately meant to help people fight for better salaries based on their job title/category. 

# Reflection
So far the collection of data went smoothly. The actual methods to investigate the research question will be ironed out later in the semester. However, we should be poised to effectively answering and visualizing the research question.


# References

Bailey, E. N., Miyata, K., & Yoshida, T. (2019). Gender composition of teams and studios in video game development. Games and Culture, 16(1), 155541201986838. https://doi.org/10.1177/1555412019868381

Buck, A. R. (2022). The price of consent: Identity wages in the games industry. Journal of Contemporary Ethnography, 51(6), 868–894. https://doi.org/10.1177/08912416221085558