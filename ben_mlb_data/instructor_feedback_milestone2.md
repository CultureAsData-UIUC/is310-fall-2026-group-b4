# Instructor Feedback for Milestone 2

You have a strong initial dataset with substantial computational work, and I appreciate the care you have shown around race. You recognize that nationality is not race and that you should not infer someone’s race from their name, photograph, or country of origin. That is an important methodological decision, and it could become a central part of your project.

## Initial Custom Dataset

One row per contract signing is a sensible starting point, but the inclusion boundaries need clarification. The source article contains 74 slides, including eighteen trades. Your scraped file therefore contains 56 nontrade slides, while the final dataset contains 42 Bleacher-derived rows and thirteen hand-added rows.

I would explain how you moved between those stages:

- Which nontrade source slides were excluded, and why?
- Why were the thirteen hand-added contracts included?
- Do extensions and minor-league contracts count?
- How were contracts with missing years or dollar values handled?
- Does the dataset cover every eligible signing in the article or a selected subset of the offseason?

For example, Brent Rooker’s extension appears in the final dataset. You may decide that extensions belong in the project, but they are different from free-agent signings. The project title and inclusion rules should reflect that choice, and a transaction-type field could help preserve the distinction.

### Provenance and Manual Additions

The scraper preserves useful evidence in `scraped_all.csv`, but much of that information disappears from `contracts.csv`, which retains only `source_id`.

The thirteen `HAND` records especially need record-level sources. A reader should be able to determine where each contract amount, term, and biographical value came from without reconstructing the process across several intermediate files.

I would preserve:

- The contract source URL and relevant slide or article section.
- Whether the record was scraped, manually corrected, or manually added.
- A note explaining corrections.
- The source and definition for the biographical field.
- The date checked and any unresolved uncertainty.

Manual research is a valuable part of this project. The goal is to make those decisions visible and reproducible, rather than leaving them only in the final CSV.

### Nationality and the Research Question

I like the pivot toward nationality, and I would encourage you to pursue that direction for the final project. I realize you wanted to explore race, but I think this pivot is more promising and that you will likely struggle to find any data that gets at race in the way you envision. You might instead write about this challenge in your final data essay and also consider how different sources describe players’ national affiliations and how you want to represent those descriptions in your dataset.

Your current values—such as `American`, `Dominican`, `Japanese`, `Mexican-American`, and `Cuban-American`—raise an interesting question: what does nationality mean in each case? These descriptions might refer to birthplace, citizenship, family background, international representation, or how a player describes himself. Rather than forcing them into one consistent category, I would preserve those distinctions where your sources support them.

You could keep the original source description alongside separate fields for relevant affiliations, then add your own interpretation of how you would describe the player’s nationality for this project. For example:

- What affiliation does each source report, and what kind of source is it?
- Does the player describe his own affiliation differently?
- Which label or combination of labels would you use in your analysis?
- Why did you choose that representation?
- Where are you uncertain, or where do sources disagree?

I would make your assessment explicitly yours rather than presenting it as a definitive statement about the player’s identity. That could include multiple labels, an unresolved classification, or a note explaining why you decided not to collapse different descriptions. You do not need to infer missing affiliations from names or photographs.

A separate mapping file could work well here. It could connect each player’s identifier to source descriptions, your chosen labels, and a short explanation of your decisions. If your assessment changes as you research, preserve what changed and why. This would make the classification process part of your cultural analysis rather than treating nationality as a straightforward fact you simply collected.

With 55 contracts, I would begin with a few carefully documented cases and examine how different ways of grouping players change the picture. Does a pattern look different when you use birthplace, international representation, or your own combination of affiliations? Some groups will be too small for meaningful salary comparisons, but those cases can still help you explain what a single nationality label would obscure.

### Contract Values and Performance Measures

Your calculated average annual value is a useful starting point, and you already recognize that it does not capture every feature of a contract. Deferrals, options, incentives, opt-outs, and uneven annual payments can complicate the relationship between total value and yearly compensation. A `contract_note` field would help preserve those qualifications.

For comparing batters and pitchers, WAR provides a shared exploratory measure in your current dataset. I would retain `war_type` and explain that the underlying calculations differ. You could begin with a plot of `aav_usd_m` against `war_2024`, then separate batters and pitchers to see whether the patterns change.

For more detailed analysis, use measures appropriate to each group: OPS and plate appearances for batters, and ERA, innings pitched, saves, or pitching strikeouts for pitchers. Avoid treating different measures as interchangeable simply because they occupy similar positions in a table.

Keep the interpretation cautious. Contracts reflect expectations about future performance, age, position, market conditions, injury history, and other considerations. One season of performance cannot explain a contract by itself.

The three players without 2024 MLB statistics are also worth documenting. Missing statistics may reflect a different league or the absence of a qualifying MLB season. Preserve the reason where you can rather than replacing missing values with zero.

## Auditing Masella’s Dataset

Masella’s thesis and replication files seem like a particularly useful audit target because they directly influenced your research design. Merging Baseball-Reference statistics into your records is valuable augmentation, but the audit should go further by investigating how an existing dataset was constructed.

I would focus on questions such as:

- How does Masella define the sample and an eligible contract?
- How are annual salary, contract length, and performance measured?
- Where do the racial classifications come from?
- Were identities self-reported, described by another source, or assigned by the researcher?
- How were ambiguous, multiracial, Latino, or international cases handled?
- Which players were excluded or could not be classified?
- Do the data and code reproduce the reported results?
- What changes when you try to apply the same approach to the 2024–25 offseason?

This would connect the audit directly to your own decisions about contracts, player identity, and comparison.

Contacting Masella could be useful, but I would first read the paper and accompanying documentation carefully. If the classification method remains unclear, you could send a focused question about the sources, coding rules, and handling of difficult cases.

Whatever you learn should inform your evaluation of the method. You do not have to adopt a classification simply because another researcher used it. Explaining why a method does or does not fit your project could itself be a strong audit finding.

## Computational Work and Reproducibility

The scraper and merger demonstrate substantial work. The main issue is that the committed code does not yet reproduce the submitted `contracts.csv`.

For example:

- `merge_stats.py` writes `my_contracts.csv`, while the README identifies `contracts.csv` as the final output.
- The script uses `ethnicity_stated`, while the submitted file contains `nationality`.
- The thirteen hand-added records and their associated corrections are not incorporated through a documented workflow.

I would create one current process that reads the preserved scraped data, applies corrections and additions from a separate file, merges performance statistics, and writes the final dataset.

That corrections file could include the player identifier, field being changed, revised value, source, and reason. This would preserve manual judgment while making the final output reproducible.

Name matching also deserves attention. Removing accents and punctuation helps, but it cannot resolve every case where two players share a name or one player appears under multiple variants. Baseball-Reference’s `Player-additional` identifier could help you retain confirmed matches in the final dataset.

You do not need an elaborate software package. Clear input files, a working script, and instructions explaining the order of operations would address the most important gaps.

## Scholarship and Reflection

Masella’s work is directly relevant and clearly influenced your dataset. The Census/BLS methodology also provides useful context for distinguishing race, ethnicity, and national origin, though it serves a different purpose from scholarship about baseball labor.

I would add one or two scholarly sources on baseball salaries, migration and international recruitment, or racial classification in sports research. Use them to inform your decisions—for example, how to define the population, compare contracts, or understand the limits of demographic categories—rather than only adding them to the bibliography.

Your README already contains thoughtful decisions and limitations. I would expand the reflection around how the project changed as you worked:

- What did you learn when race proved difficult to represent?
- Why did nationality not resolve the original question?
- Which records required manual correction, and what did those cases reveal?
- How did joining contract and performance data change what you wanted to investigate?

I also did not see an AI-use statement. If AI contributed, explain what it did and how you checked or revised its outputs. If you did not use AI, a brief statement would clarify that.

## Priorities for the Final Project

For the next stage, I would prioritize:

1. Clarifying the research question and defining the biographical field consistently.
2. Auditing Masella’s classification methods and deciding what they mean for your project.
3. Documenting inclusion rules, hand-added contracts, corrections, and record-level sources.
4. Updating the workflow so it reproduces the submitted dataset and preserves confirmed player identifiers.
5. Developing an exploratory analysis that distinguishes player roles, contract terms, and reasons for missing performance data.
6. Expanding the scholarship, reflection, and AI-use documentation.

You have already done substantial collection and transformation work. Making those decisions traceable—and explaining what the data cannot establish—will strengthen the project and give you a clearer basis for expanding it.
