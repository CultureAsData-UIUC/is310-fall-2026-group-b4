# Instructor Feedback for Milestone 2

I like the focus on WNBA labor, compensation, and working conditions, and I appreciate how carefully you distinguish between different kinds of evidence. Your project offers a useful way to investigate what basketball statistics leave out about players’ working lives and the institutions that shape them.

The strongest feature so far is your attention to uncertainty. Separating source descriptions, documented responses, and unresolved questions helps avoid treating an official announcement, an allegation, and an established finding as equivalent. I also appreciate your recognition that something being absent from a statistics dataset does not automatically establish discrimination.

For the next stage, I would focus on making the dataset structure, source verification, and computational workflow as clear as those methodological intentions.

## Initial Custom Dataset

Your submission includes eleven contextual records, a source tracker, and substantial documentation. This is a useful beginning, but I would explain why collection remains at this stage and give a feasible plan for developing it.

Additional records should help you investigate a particular question or introduce useful perspectives. For example, would you learn more by following a few labor issues across institutional statements, reporting, and player responses, or by comparing how different issues are represented? That choice will help determine what to collect next.

### Unit of Analysis and Related Records

I’m curious what you want one row to represent: an event, a source, or a claim about an event? Those are different units, and the distinction matters when several sources discuss the same development.

For example, multiple records might concern provisions of the same collective bargaining agreement. Keeping those records can be useful, especially if they offer different perspectives, but they should not automatically count as separate events.

I would add stable record identifiers and consider a related-event field that connects records about the same development. A source identifier could then distinguish the publication supporting each record. This would let you preserve multiple accounts without losing track of their relationships.

### Dates and Historical Context

Your documentation recognizes that publication dates and event dates differ, but the JSON currently uses one date field. I would separate those dates where the source supports doing so.

If you only know the month or year, preserve that level of precision rather than supplying an exact date. You could also include a short note explaining uncertain or approximate dates.

Similarly, clarify which records fall within the stated 2023–2025 focus and which provide earlier historical context. Earlier material may be essential to understanding later developments, but readers should be able to distinguish those roles.

### Issue Categories and Interpretation

The issue categories help organize the collection, but I would explain how you assigned them. What makes a record primarily about compensation, benefits, workplace treatment, or media visibility? How do you handle a record that concerns several of those issues?

You could allow multiple categories or distinguish a primary issue from related ones. The important thing is to explain the decision and avoid making overlapping concerns appear unrelated simply because they occupy different categories.

Your uncertainty notes are already a strength. I would develop them with examples of difficult decisions: a source whose claims required qualification, competing accounts of an event, or a category you changed after reading more closely. Those examples would make your own interpretive work more visible.

### Provenance and Verification

The JSON contains eleven records with eleven unique source URLs, while the source tracker contains nine entries. Please reconcile the two files so that readers can trace the evidence and review status for every record. A stable source identifier would make that connection easier to maintain as the collection grows.

I appreciate that the tracker distinguishes checking a title or URL from reading the full source. Keep that distinction, and explain what each verification status establishes.

Reading a news report confirms what that report says; it does not independently establish the truth of every claim within it. Continue attributing allegations, projections, and institutional statements to the people or organizations making them. Where sources disagree, preserving that disagreement may be more useful than choosing one account as definitive.

## Computational Work

The README describes Python validation, but I don’t see the corresponding script or notebook in the submitted folder. Please include that artifact, along with instructions and any dependencies needed to run it.

For this dataset, useful checks could include:

- Whether each record contains the required fields.
- Whether record and source identifiers are unique.
- Whether repeated URLs represent accidental duplicates or intentional reuse.
- Whether dates follow the documented format.
- Whether every dataset source appears in the tracker.
- Whether issue categories and verification statuses use consistent labels.

The code does not need to be elaborate. I want to see how computation helps you maintain the collection and identify records that need closer attention. It is also worth explaining what the checks cannot establish: valid JSON and complete fields do not guarantee that a claim is accurate or that an interpretation is justified.

## Audit Plan

The documentation identifies a type of basketball dataset you might audit, but the next step is to name a specific source. Explain who created it, what it was designed to represent, and why it provides a useful comparison with your collection.

I would be careful about assuming that a statistics-focused dataset should contain every aspect of players’ lives. Its omissions can still be worth investigating, but their significance depends on the dataset’s purpose and the claims people make with it.

Questions you might explore include:

- What does one record represent?
- Which players, seasons, leagues, or institutions are included?
- Which aspects of basketball become visible through its fields?
- What kinds of questions about compensation or working conditions can it support?
- What context would someone need before using it to make broader claims about players’ experiences?

Your contextual records do not need to join directly to player-statistics rows. Comparing what the two data structures can represent may be more productive than forcing a record-level merge. For example, you could examine how an institutional change appears in your collection and whether a statistics dataset could register that change at all.

## Scholarship and Reflection

You list several scholarly publications, which gives you a useful starting point. I would now explain how selected sources inform your choices. Do they help distinguish forms of inequality, identify relevant institutional perspectives, or complicate how you interpret compensation and working conditions?

The scholarship should help shape the categories and analysis rather than remain only a list of references.

I would also expand the reflection in your final data essay with specific examples from the research process:

- Which records were hardest to interpret or verify?
- Did different sources describe the same issue differently?
- Did your categories change as you collected material?
- What was lost when a complex development became one JSON record?
- What has limited collection so far, and how will you address that?
- What feedback would help you decide the next direction?

If AI assisted with research, categorization, writing, or code, explain what it contributed and how you checked or revised its outputs. Concrete examples would help distinguish your own decisions from suggestions you received.

## Priorities for the Final Project

For the next stage, I would prioritize:

- Clarifying the unit of analysis and connecting related records.
- Separating publication and event dates while preserving uncertainty.
- Reconciling the source tracker and documenting verification levels.
- Including the computational artifact described in the README.
- Identifying a specific audit target and a feasible comparison method.
- Developing a focused collection plan and connecting scholarship to your decisions.

You have a thoughtful foundation, especially in how you handle uncertainty and different perspectives. Making the research process traceable will help readers understand how those intentions are reflected in the actual records.
