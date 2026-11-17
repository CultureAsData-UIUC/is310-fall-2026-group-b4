# Instructor Feedback for Milestone 2

You have created a promising initial dataset, and several of the individual records show careful attention to how gender is represented through marriage, beauty, authority, domestic work, physical strength, and women's agency. The dataset is a strong start for Milestone 2. I would clarify how the ten films and five scenes per film were selected and make the interpretive method more consistent as you plan further collection.

The main areas still needing development are the distinction between depicting and challenging a stereotype, documentation of the sampling and evidence, a concrete audit method for the existing movie-dialogue project, a fuller reflection, and engagement with published scholarship.

## Initial Custom Dataset

Overall, you have a strong initial dataset and the README clearly explains that you selected ten films and five scenes from each. But it does not yet explain why you chose these particular films or these particular scenes.

I would suggest documenting:

- Why these ten films belong together
- Whether you selected them because they were popular, personally familiar, centered on princesses, produced by particular studios, or covered a particular period
- Why *The Nightmare Before Christmas* and *Shrek* belong in the same comparison as the Disney princess films
- How you found candidate scenes
- Why you stopped at five scenes per film
- Whether you selected the most obvious examples, the first five you encountered, or scenes representing different themes
- Whether scenes without clear stereotypes were considered and excluded

Five scenes per movie creates a balanced dataset, but it does not show how common stereotypes are within each film. Because the scenes were purposively selected, the result that forty scenes are labeled `Challenges` and ten are labeled `Reinforces` describes your selected sample rather than the complete content of the movies. Indeed, the most important methodological issue is that `reinforces_or_challenges` currently shifts between several levels of interpretation.

For example, the matchmaker scene in *Mulan* clearly depicts and enforces the stereotype that women should become obedient wives, but the record labels it `Challenges`, presumably because the larger film ultimately rejects that expectation. Similarly, a character may express a stereotype, another character may resist it, and the overall film may frame the event critically. Those are three different claims.

I would suggest separating them into fields such as:

- `stereotype_depicted`: What gendered expectation appears in the scene?
- `character_response`: Does a character accept, resist, complicate, or remain subject to it?
- `narrative_treatment`: Does the scene or larger film appear to endorse, criticize, complicate, or leave the stereotype unresolved?
- `interpretive_confidence`: How certain are you about that reading?

You do not have to use these exact names, but the documentation should explain whose perspective the classification represents. Separating the stereotype's presence from the narrative's response would make your interpretations easier to understand and would preserve cases where a film both reproduces and criticizes a stereotype. I think it would also be helpful to think about the category of stereotype more critically. Who is defining a stereotype exactly? Is it your definition or one you are adopting from elsewhere? For instance, many of these movies are likely tagged in TV Tropes website, so you might compare your definitions and tagging to those there to help ground your approach. But generally, I would encourage you to think carefully about stereotypes as culturally and historically-specific categories, rather than universal ones.

In terms of the dataset, the timestamp ranges and paraphrased evidence give readers a useful path back to each scene. I would strengthen that traceability by recording the version or platform used, since timestamps can differ across releases, streaming services, and edits.

You might also preserve a short line of dialogue or a more specific description of the visual action when it is necessary to support the interpretation. The current `evidence` field often repeats the scene description in slightly different language. A clearer distinction might be:

- What literally happens or is said
- What stereotype you infer from it
- Why you interpret the narrative as reinforcing or challenging it

The README says the interpretations are based on your opinions and online research, but it does not identify that research. Please add source links for any plot summaries, transcripts, commentary, or other materials used. Also distinguish scenes you watched directly from interpretations based primarily on secondary descriptions.

Some entries may benefit from an uncertainty option. For example, pressure to marry, interpersonal control, narrative conventions, and discrimination overlap but are not always identical. You could retain difficult cases and mark them `mixed` or `uncertain` rather than forcing every scene into a binary category.

## Auditing the Gender Equality in Movies Project

I think the Gender Equality in Movies dataset is a good option and the GitHub repository you linked seems to be a very substantial computational project rather than a single CSV. In particular, the project seems to convert movie scripts into structured dialogue, assigns character genders, and applies sentiment and emotion analysis. So your audit should investigate how those transformations were made.

Questions worth asking include:

- Who created the project and for what purpose?
- Which movies and genres are included, and why?
- Where did the scripts come from?
- Are the scripts complete and legally reusable?
- How were characters matched to dialogue?
- How was gender assigned, and why is it represented only as male or female?
- What happens to unknown, nonbinary, nonhuman, or ambiguously gendered characters?
- How many records are missing gender or dialogue information?
- Which NLP models or dictionaries produced the sentiment and emotion scores?
- Were those tools validated for screenplay dialogue?
- Are the processed files reproducible from the scripts and code?
- Is there a license allowing reuse or redistribution?

Generally though, I think the Gender Equality in Movies repository should be treated first as an existing dataset to audit, not as a set of rows to append directly to your scene dataset since your unit of analysis differs from theirs. Your rows represent interpreted scenes, whereas their project processes scripts and dialogue associated with characters, assigns binary gender labels, and generates sentiment or emotion scores. A line of dialogue cannot be merged directly with one of your scene interpretations simply because both concern gender in movies.

I would recommend this approach:

- Audit the existing project's provenance, methods, and categories.
- Identify whether any of your ten films appear in its processed data.
- For overlapping films, summarize both datasets at the **movie level** rather than attempting a row-level merge.
- Compare what each method makes visible.

For example, your movie-level summary might include the number of selected scenes coded as reinforcing, challenging, mixed, or uncertain and the major stereotype themes you identified. The existing project might provide dialogue counts, character-gender representation, or emotion measures by movie. You could then ask whether a film that appears to give women more dialogue also challenges gender stereotypes in the scenes you selected. The two measures will not necessarily agree, and that disagreement could be an interesting finding.

If there are few or no overlapping films, you can still audit the existing dataset without forcing a quantitative comparison. The audit could explain why its coverage does not support your question and how your scene-level approach captures narrative and visual context that dialogue-level analysis misses.

## Computational Work

The current Python script successfully creates the CSV, which demonstrates a clear transformation from your structured records into a reusable file. For the final project, you might add a small validation or analysis script that checks:

- Fifty unique scene IDs
- Five records per movie
- Valid timestamp formatting
- Allowed values for interpretive categories
- Missing evidence or descriptions
- Counts by film and category

You could then create one or two visualizations showing the distribution of your revised categories or themes. Keep in mind that equal scene counts and purposive selection mean these charts describe your coded sample, not the full frequency of stereotypes within each movie.

## Scholarship and Reflection

The current README does not include the required two or three published scholarly sources. I would suggest finding scholarship on animated film, Disney or princess narratives, gender stereotypes, feminist film analysis, or computational approaches to gender representation. The scholarship should help define your categories or complicate your interpretation rather than only confirm that gender stereotypes exist.

The reflection also needs more development for the final essay. In addition to saying that interpretations are subjective, I would discuss:

- Which scenes were hardest to classify
- Whether your understanding of `reinforces` and `challenges` changed during collection
- What was lost when a complex scene became one row
- Whether online summaries differed from your own viewing
- How selecting exactly five scenes shaped the patterns you found
- What feedback would help you resolve uncertain cases

I did not see an AI-use statement. If you used AI to identify scenes, please explain what it contributed and how you verified or revised the outputs. If you did not use AI, a brief statement confirming that would also clarify the methodology.

## Priorities for the Final Project

For the next stage, I would suggest prioritizing:

- Explaining why the ten films and five scenes per film were selected.
- Separating the presence of a stereotype from a character's and narrative's response to it. Also adding source provenance, direct evidence, version information, and uncertainty where appropriate.
- Auditing the dialogue project's script sources, gender assignment, NLP methods, coverage, and reuse conditions. Then comparing the projects at the movie level only where films overlap.
- Adding validation or summary code and a small number of appropriately qualified visualizations.
- Connecting two or three scholarly sources to the coding method and interpretation.
- Expanding the reflection and adding an AI-use statement.

Overall, the initial dataset gives you a solid foundation and a useful close-reading perspective. The strongest final version will make your interpretive method more transparent, preserve ambiguity rather than forcing every scene into a binary judgment, and use the audit to show what scene analysis can reveal that dialogue-level computational analysis leaves out.
