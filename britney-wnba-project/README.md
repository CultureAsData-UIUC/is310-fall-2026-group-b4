# WNBA Gender Inequality and Working Conditions

## Project Overview

This project examines gender inequality in the Women's National Basketball Association (WNBA), focusing on player compensation, collective bargaining, workplace treatment, benefits, working conditions, media visibility, and commercial growth.

Rather than treating basketball as only statistics and game outcomes, this project collects contextual records about the institutions, decisions, public claims, and responses that shape players' working lives.

The project recognizes that statistics alone may not explain the institutional and social conditions surrounding professional athletes. By collecting contextual information, it aims to document issues that may be overlooked in traditional basketball datasets.

## Research Question

What do records about WNBA compensation, benefits, workplace treatment, and working conditions reveal that a statistics-focused basketball dataset may leave out?

## Dataset Description

- **Dataset file:** `basketball_data.json`
- **Source tracker:** `source_tracker.csv`
- **Current dataset size:** 11 records from 11 unique source URLs
- **Primary research period:** January 1, 2023–December 31, 2025

The dataset is an initial collection and does not yet meet the intended target of approximately 50–100 data items. Earlier material, including the 2020 Collective Bargaining Agreement (CBA), is included as historical context when it helps explain developments during the primary research period.

Each record contains the following fields:

- `event_title`: The event, decision, claim, or development being documented.
- `date`: The recorded date, which may represent a publication date or event date; these should not be treated as interchangeable.
- `institution_involved`: The organization or institution connected to the record.
- `issue_category`: The main topic assigned to the record.
- `source_title`: The title of the source.
- `source_url`: A link to the source.
- `source_description`: A summary of the source's relevant information.
- `documented_response`: A recorded response from an involved institution or other relevant party, when available.
- `uncertainty_context`: Limitations, competing accounts, missing information, and other context needed to interpret the record responsibly.

## Research Approach and Methodology

This project follows a **Create Data from Scratch** approach. Rather than starting with an existing dataset and modifying it, the project builds a contextual collection from publicly available cultural materials related to the WNBA.

The collection uses a source-based, purposive approach. Sources are selected because they provide information relevant to the research question, rather than through random sampling or an attempt to represent every WNBA event.

The project focuses on materials from journalism, official league and players' association announcements, public statements, and scholarly research. These materials help document institutional decisions, workplace issues, player concerns, and the league's commercial development.

The primary research period is 2023–2025. Earlier material is included only when it provides historical context for developments during that period.

The goal is to preserve the context surrounding each record, including the source's perspective, the issue being discussed, and any documented responses or uncertainty.

## Inclusion Criteria

A record should:

1. Have a direct connection to the WNBA and the project's research question.
2. Address compensation, collective bargaining, benefits, workplace treatment, working conditions, media visibility, sponsorship, or related institutional decisions.
3. Have a traceable source that provides enough information to describe the record.
4. Preserve relevant context, including the source's perspective and any documented responses.
5. Distinguish reported facts from allegations, opinions, projections, and interpretations.

## Exclusion Criteria

A record should be excluded or reconsidered when it:

- Has no traceable source or sufficient supporting context.
- Duplicates an existing record without adding meaningful information.
- Concerns an unrelated league or event without a clear connection to the research question.
- Treats an allegation as a proven finding without supporting evidence.
- Infers a person's identity, motivation, or experience without evidence.
- Confuses a source's publication date with the date of the event it describes.

## Data Collection and Transformation

The project uses a two-stage transformation process.

### Stage 1: Cultural Material to Working Representation

Relevant material is collected from journalism, official league and players' association announcements, public statements, and scholarly research. Notes identify the source, its perspective, the event or claim being documented, and any uncertainty or missing context.

Sources are considered based on their relevance to the research question and their ability to provide useful contextual information. The collection is not intended to be a statistically representative sample of all WNBA events.

### Stage 2: Working Representation to Structured Data

The notes are converted into structured JSON records using the fields described above. A source tracker records publication and event dates, source type, topic, perspective, potential dataset record, and verification status.

Python is used to validate the JSON structure, check for missing fields and duplicate source URLs, and summarize patterns across the dataset. Categories are analytical choices rather than neutral facts; they may be revised as the collection grows.

The project should preserve the distinction between what a source explicitly documents and what the researcher interprets from it.

## Computational Tools and Their Limitations

The project uses several digital tools to support research and data organization:

- **Python:** Used to validate JSON formatting and support basic data checks.
- **JSON:** Used to organize the contextual records into a structured format.
- **CSV:** Used to maintain source information, including publication details, perspectives, and verification notes.
- **GitHub:** Used to store project files and document project development.
- **ChatGPT:** Used primarily for brainstorming, discussing the research focus, reviewing project descriptions, and occasional troubleshooting.

These tools support organization and review but do not replace source evaluation or human interpretation. For example, valid JSON formatting does not guarantee that the information inside a record is accurate. Automated tools may also overlook context, misinterpret claims, or categorize information incorrectly. Sources and interpretations therefore require human review.

## Initial Dataset Patterns

The current collection includes records about:

- Working conditions and maternity-related policies.
- A pregnancy-discrimination complaint and the need to distinguish allegations from established findings.
- Charter travel and other workplace conditions.
- Sponsorship and media visibility.
- Attendance, viewership, merchandise, and commercial growth.
- Collective bargaining and player compensation.

These records show that the project brings together different types of evidence. For example, reported audience growth documents commercial expansion, while union statements and collective bargaining coverage document disputes about how players' priorities and economic interests are addressed. Neither type of evidence alone establishes the overall extent or cause of gender inequality.

The collection is still small, so these patterns are preliminary rather than representative conclusions about the entire league.

## Planned Dataset Audit

The project will compare its contextual records with a specific statistics-focused basketball dataset. The comparison dataset must be identified and documented before the audit is considered complete.

The audit will examine:

1. **Coverage:** Which players, teams, seasons, and events appear in both datasets?
2. **Missing context:** Which labor issues, policies, public claims, institutional responses, or workplace experiences are not represented in the statistics-focused dataset?
3. **Data structure:** What counts as a record in each dataset, and which fields, units, dates, and categories are available?
4. **Research questions:** Which questions can be answered with performance statistics, and which require contextual sources?
5. **Limitations:** How do collection methods and category choices shape what researchers can see?

A contextual event missing from a statistics dataset is not automatically evidence of discrimination or intentional exclusion. The audit will explain what each dataset was designed to capture and what its structure makes difficult to investigate.

## Limitations and Uncertainty

- **Small collection:** The current 11 records are an initial dataset, not a comprehensive account of WNBA gender inequality.
- **Source selection:** Publicly available reporting may overrepresent highly visible controversies, prominent players, and events that attract substantial media attention.
- **Different evidence types:** Official announcements, journalism, opinion pieces, allegations, and scholarly findings have different purposes and evidentiary strengths.
- **Competing perspectives:** The league, players' association, individual players, journalists, and researchers may describe the same issue differently.
- **Date ambiguity:** An article's publication date may not be the date an event occurred. Uncertain dates should remain explicitly qualified.
- **Interpretive categories:** Categorization involves researcher judgment and can oversimplify issues that overlap.
- **Missing information:** Silence in a source does not prove that an event did not occur, and absence from a dataset does not by itself prove bias.
- **Changing conditions:** League policies, commercial arrangements, and collective bargaining can change over time. Claims must be interpreted in the period to which they apply.

The current collection should therefore be understood as an initial research resource. Its records provide examples of issues and perspectives, not a complete measurement of inequality across the league.

## Research Sources

### Primary and Journalistic Sources
- WNBA. "Transcript - WNBA-WNBPA Conference Call."
  https://www.wnba.com/news/transcript-wnba-wnbpa-conference-call

- WNBA. "WNBA Set to Institute Full Charter Program During 2024 Season."
  https://www.wnba.com/webview/news/charter-flight-program-2024

- WNBA. "WNBA and WNBPA Reach Tentative Agreement on Groundbreaking Eight-Year Collective Bargaining Agreement." January 14, 2020.  
  https://www.wnba.com/news/wnba-and-wnbpa-reach-tentative-agreement-on-groundbreaking-eight-year-collective-bargaining-agreement

- ESPN. "Sparks' Dearica Hamby Sues WNBA, Aces Alleging Discrimination."  
  https://www.espn.com/wnba/story/_/id/40839309/sparks-dearica-hamby-sues-wnba-aces-alleging-discrimination

- Associated Press. Report on WNBA sponsorship opportunities and unequal brand visibility. November 17, 2024.  
  https://apnews.com/article/6706195c98ebae41e8369cd978bf0a14

- Reuters. "WNBA regular-season attendance up 48% in 2024." September 27, 2024.  
  https://www.reuters.com/sports/wnba-regular-season-attendance-up-48-percent-2024-09-27/

- WNBA. "WNBA Delivers Record-Setting 2024 Season."  
  https://www.wnba.com/news/wnba-delivers-record-setting-2024-season

- NBA/WNBA. Announcement of long-term media rights agreements. July 24, 2024.  
  https://pr.nba.com/wnba-walt-disney-company-amazon-prime-video-nbcuniversal-media-agreements/

- Associated Press. Report on the WNBPA's decision to opt out of the existing collective bargaining agreement. October 21, 2024.  
  https://apnews.com/article/3fd6c2eb9924689d3a0ea929d309d605

- Reuters. "WNBA has failed to meet players' priorities in CBA talks, union says." July 17, 2025.
https://www.reuters.com/sports/wnba-has-failed-meet-players-priorities-cba-talks-union-says-2025-07-17/

Sports Business Journal. "It's time for player salaries to catch up with WNBA's growth." June 9, 2025. This is an opinion piece, not a neutral statistical finding.
https://www.sportsbusinessjournal.com/Articles/2025/06/09/its-time-for-player-salaries-to-catch-up-with-wnbas-growth/

Published Scholarly Research

These publications provide research context. They are not substitutes for verifying the primary sources attached to individual dataset records.

Banet-Weiser, Sarah. "Hoop Dreams: Professional Basketball and the Politics of Race and Gender." Journal of Sport and Social Issues (1999).
https://doi.org/10.1177/0193723599234004

McDonald, Mary G. "Queering Whiteness: The Peculiar Case of the Women's National Basketball Association." Sociological Perspectives 45, no. 4 (2002): 379–396.
https://doi.org/10.1525/sop.2002.45.4.379

Arutiunova, Margarita, and Thadeu Gasparetto. "Wage Dispersion and Sports Performance: Does Gender Matter?" Gender in Management 38, no. 8 (2023): 1153–1171.
https://doi.org/10.1108/GM-10-2022-0341

Agha, Nola, David J. Berri, Akash Bhat, and Jennifer Van Gilder. "The Effect of National Origin and Skin Color on Playing Time in the WNBA." Journal of Sports Economics 25, no. 6 (2024): 735–752.
https://doi.org/10.1177/15270025241260030

Minuci, Eduardo G., and Zachary Rodriguez. "Determinants of Contracts and Wages in the Women's National Basketball Association." Journal of Sports Economics (2026).
https://doi.org/10.1177/15270025261474143

##Project Files

basketball_data.json — structured contextual dataset.

source_tracker.csv — source metadata, perspective, and verification notes.

README.md — project scope, collection criteria, methods, and limitations.

ai-chat-log.md — documentation of AI assistance during the project.

Next Steps and Potential for Scaling

The current dataset contains 11 contextual records. Although it does not meet the intended initial target of approximately 50–100 items, it provides a starting point for examining how labor conditions, compensation, workplace policies, media visibility, and commercial growth are documented in the WNBA.

Rather than treating the current collection as a comprehensive representation of the league, future development could expand it through a combination of automated collection methods and human review.

Potential Computational Methods

Web scraping: Public news archives, league announcements, and players' association websites could be searched for relevant articles and announcements. Scraping would require attention to website terms, access restrictions, and changes in page structure.

APIs and existing datasets: Sports and news APIs could provide larger collections of articles, league information, and statistics. These sources could be combined with the contextual records to compare what performance-focused datasets capture with what they leave out.

Keyword and pattern matching: Python could identify recurring terms related to salaries, collective bargaining, maternity benefits, sponsorship, media coverage, and workplace conditions. This could help organize large collections of potential sources.

Large language models: AI tools could assist with summarizing potential sources, identifying recurring topics, and suggesting preliminary categories. However, generated summaries and classifications would require human verification to prevent inaccurate interpretations or the treatment of allegations as established facts.

Combining Contextual and Existing Data

A future version of the project could combine this contextual dataset with a larger statistics-focused WNBA dataset. Player performance, attendance, and other quantitative measures could be examined alongside records about compensation, workplace policies, collective bargaining, and media visibility.

This approach would allow researchers to investigate questions that a statistics-only dataset may not answer. For example, performance statistics may document what happens on the court, while contextual records may provide information about the policies and institutional decisions that shape players' working conditions.

Challenges and Ethical Considerations

Scaling the collection would introduce several challenges:

Automated searches may collect duplicate, irrelevant, or unreliable sources.

Keyword searches may miss relevant information that uses different terminology.

Automated categorization may remove important context or oversimplify competing perspectives.

Sources may contain allegations, opinions, or institutional statements that require careful distinction from verified findings.

Public reporting may overrepresent prominent players and highly publicized controversies.

Human review would therefore remain necessary to verify sources, preserve uncertainty, distinguish event dates from publication dates, and document competing accounts.
