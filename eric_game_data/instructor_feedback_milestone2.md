# Instructor Feedback for Milestone 2

I like the focus of this project and I'm impressed by the amount of computational work you have already completed. The project also has a potentially strong culture-as-data question: how do different salary datasets construct game-industry labor, and what can or cannot be learned about gendered pay from those representations?

The main issue is that the two datasets do not currently measure the same population or the same kind of salary record. The H-1B data covers employer-filed labor-condition applications for visa-sponsored positions at two U.S. companies across several years. The GLITCH data is an anonymous, self-selected, international survey of individual workers that includes gender, experience, region, and other characteristics. Comparing their overall averages would not provide reliable evidence that women are paid less than men.

This divergence does not mean you need to abandon the project. But I would strongly recommend that the final analysis should focus on auditing the differences between the datasets and making a smaller, more careful comparison among genuinely comparable records, than trying to argue these identical or easily comparable.

## Initial Custom Dataset

Overall, you have a strong foundation for your dataset. However, the records from H1BData should not be described simply as ordinary job listings. They are derived from Labor Condition Applications filed when an employer seeks authorization to employ an H-1B worker in a particular occupation and area. The wage represents an employer's wage attestation for the sponsored position. An application does not necessarily establish that a worker was ultimately hired, began the job, remained employed, or received that exact annual total in practice.

The records are therefore a valuable representation of employer-sponsored positions, but they are not a general sample of everyone employed by Epic or Rockstar. They are shaped by immigration policy and include only positions for which these companies pursued this form of visa sponsorship.

I would suggest changing the dataset description from “job listings” to something such as "H-1B Labor Condition Application salary records". The documentation should also explain:

- What an LCA is
- What the salary field represents
- Whether the amount is annual or hourly in the source
- Whether an application corresponds to one worker or may cover multiple positions
- What the records cannot tell us about actual hiring or payment
- Why visa-sponsored roles may differ from the companies' broader workforces

That provenance is essential before using the salaries as a benchmark.

### How Were the Final 100 Records Selected?

The initial scrape produced 296 adjusted records, and your categorized files retain 173 records. The final dataset then selects 100 records based partly on which jobs appear frequently in the GLITCH survey and which categories appear to contain different genders.

That selection risks building the desired comparison into the sample, and is also not currently reproducible because there is no script or selection log showing exactly which rows were retained and why.

You do not need to reduce a scraped dataset to exactly 100 rows just because the milestone suggested approximately 50–100 records. I would recommend one of two approaches:

1. Keep all records that meet clearly documented inclusion and category rules.
2. Create a reproducible comparison subset after defining the overlapping job categories, years, countries, and other relevant characteristics.

In either case, preserve the excluded records in an earlier-stage file and record the reason for exclusion. A title that is difficult to categorize could receive `Unclassified` or `Other` rather than disappearing from the data. The number and kinds of unclassified titles may themselves reveal a limitation of the category system.

I also noticed that the final dataset contains ten exact duplicate rows, and the Epic categorized file contains nine duplicates. These may be accidental duplicate records, or they may represent separate applications with the same employer, title, salary, location, and start date. The current fields do not give us enough information to tell.

The source table appears to contain additional information such as submission date, and the underlying LCA data may provide a case identifier or number of workers requested. I would preserve as many original identifying fields as possible before deciding whether repeated rows should be removed. If several applications are genuinely distinct, they may remain separate, but the unit of observation should be described as an application record rather than a unique job or worker.

### Job Categories and Interpretative Data Work

Generalizing job titles into categories is a smart way to create overlap between the datasets, but it is also one of the project's largest interpretive transformations. For example, deciding whether an animation programmer belongs under `Software Developer`, `Animator`, or another category can substantially affect the salary comparison.

I would suggest documenting:

- Every original title and its assigned category
- The rules used to assign categories
- How seniority terms such as `lead`, `senior`, `associate`, and `director` are handled
- Whether management and nonmanagement roles are separated
- Which titles remain uncertain or unclassified
- Whether the same mapping rules are applied to both datasets
- Any notes for how you decided to categorize
- Potentially an uncertainty field for jobs that you were less certain about their categorization

Similarly, a separate title-to-category mapping file could make this process visible and reusable. You might also preserve a broader category and a seniority field rather than asking one category to represent both occupation and rank.

Converting salaries into 2020 dollars is a sensible transformation, particularly because the H-1B data spans 2018–2025. The documentation should explain why 2020 was chosen and identify the CPI source and retrieval date or package version.

The comparison may become simpler if you restrict the H-1B benchmark to years overlapping the 2020–2021 GLITCH survey. That would reduce the influence of time and limit the amount of inflation adjustment required. If you retain later years, keep the original salary and adjusted salary together, as you currently do.

While the current repository includes scripts for scraping and inflation adjustment, it does not seem to have any for assigning categories, selecting the final records, or combining the company files. Those transformations should either be added to a reproducible script or clearly documented. You might even add some examples to your final data essay to help narrate how you made these decisions.

### Research Question & Reconciling the Datasets

I appreciated your transparency that your method for answering the research question is still a work in progress. One approach you might consider is using the GLITCH survey as the primary evidence for observed gender differences, and use the H-1B records as a separate contextual benchmark rather than as the expected salary everyone should receive.

Within the GLITCH data, you might create a comparison subset that is as consistent as the available fields permit. For example, you might focus on:

- Respondents in the United States
- Records from 2020 and 2021
- Full-time annual salaries rather than mixing hourly and annual pay
- Job categories that overlap with the H-1B categories
- Comparable seniority or years of experience
- Categories with enough respondents to avoid interpreting one or two people as a group pattern

Then compare salary distributions by gender within those categories. I would use counts, medians, ranges, and visual distributions rather than only means, since a small number of very high salaries can strongly affect an average.

The H-1B records could then provide a second descriptive comparison: what wage levels were represented in Epic and Rockstar's visa-related filings for similar categories during overlapping years? I would suggest though positioning that analysis as describing two companies and a specialized group of positions, not the games industry as a whole.

Generally, I think you can still investigate observed gender differences in reported salaries and ask whether patterns remain within comparable job categories. You can also study how the datasets make gender, immigration status, employer, experience, and salary visible or invisible. I would avoid claiming that a difference proves discrimination or that the H-1B salary is what a respondent “should” have earned.

This framing aligns with the caution you already identify in Bailey: a broad pay gap does not show that women earn less for the same position. Your dataset can help demonstrate why that distinction matters, while also making visible why it is so difficult to study these trends in the games industry.

## Auditing the GLITCH Survey

The GLITCH survey is a strong audit target because its design directly shapes the gender comparison. I would investigate:

- Who created and promoted the survey
- Whether there were any iterations of the survey questions or design
- How respondents encountered it
- Whether one person could submit more than once
- Which countries, currencies, years, and employment types are represented
- How salaries were converted or standardized
- How job categories and gender options were defined
- Which fields are missing and whether missingness varies by gender or region
- Whether extreme values are errors, unusual but valid salaries, or compensation measures that include different things
- Whether the public documentation explains cleaning or verification

The survey's self-selected nature does not make it useless, but it means the respondents should not automatically be treated as representative of all game workers. Because combinations of job title, location, studio size, experience, gender, and ethnicity may make an ostensibly anonymous respondent more identifiable, so I would also avoid republishing unnecessary row-level demographic information. Instead, you might aggregate small groups and use visualizations to avoid directing attention to individuals.

I do wonder if you might also consider doing at least some brief auditing of the H1B Salary Database to also help contextualize the data you've scraped. You might try to answer some similar questions, and especially try to get a sense of how the structure of that database may shape your use of this data.

## Code and Repository Organization

The scripts demonstrate substantial work, but a few changes would improve reproducibility:

- `table_scraping.py` is currently hard-coded for Rockstar even though the README describes scraping both companies.
- The script does not preserve every source column that may help distinguish repeated records.
- The category assignment, filtering, and final combination steps are not scripted.
- The raw CSV files require `cp1252`, but that encoding is not explained in the README.
- `requirements.txt` appears to be saved with an unusual encoding and may not work normally with `pip install -r requirements.txt`.
- The output paths in `inflation_adjust.py` depend on where the script is run.

You do not need to create an elaborate software package. One clear script that moves from the preserved raw files to the categorized and combined analysis data would make the most important transformations reproducible. Happy to help troubleshoot any technical bugs too!

## Scholarship and Reflection

The Buck and Bailey sources are relevant and already help complicate a simplistic pay-gap argument. However, the reflection is currently only a few sentences and mainly says that collection went smoothly and the analytical method will be developed later. For the final version, I would reflect on the decisions that have already shaped the data: why these companies were selected, how job categories were created, what was lost when records were excluded, why the two datasets are difficult to compare, and how your research question changed after understanding the sources.

I did not see an AI-use statement. If you used AI, please explain what it contributed and how you checked or revised its outputs. If you did not use AI, a brief statement confirming that would make the process clear.

Also check the dates in the prose and references: the text refers to Bailey as 2022 in one place, while the reference lists the article as 2019.

## Priorities for the Final Project

For the next stage, I would suggest prioritizing:

- Correctly describing the H-1B records as LCA salary records rather than ordinary job listings.
- Replacing the hand-selected 100 rows with transparent and reproducible inclusion rules.
- Preserving identifiers and source fields needed to understand repeated records.
- Documenting and scripting the job-category transformation.
- Auditing the GLITCH survey's provenance, scope, categories, missingness, and privacy risks.
- Restricting the gender analysis to more comparable GLITCH records and reporting descriptive differences rather than claiming causal discrimination.
- Treating H-1B wages as a separate contextual benchmark for two companies and visa-sponsored positions.
- Expanding the reflection and adding an AI-use statement.
- Cleaning the repository and requirements file so the workflow can be reproduced.

Overall, this is a compelling topic with substantial collection and transformation work. But I think the strongest final version will not rely on a single average or claim to prove discrimination. Instead, it will show how two very different salary datasets represent workers differently, carefully document the subset that can be compared, and use those differences to explain both the observed gender patterns and the limits of the available evidence.
