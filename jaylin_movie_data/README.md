# Gender Stereotypes Within Animated Movies

## Overview:

The dataset I created contains 50 rows from 10 movies specifically targeting gender stereotypes and discrimination in animated movies. Additionally, each row represents one scene from the movie.

## Columns in my Dataset:

- `scene_id`
- `movie_title`
- `release_year`
- `timestamp`
- `scene_description`
- `gender_stereotype`
- `discriminatory_action`
- `evidence`
- `reinforces_or_challenges`

## Method:

I selected 10 movies to make a dataset of with five scenes from each movie. I collected data such as the gender stereotype, discriminatory action that happened, and what potentially evidence is shown in the scene. I also have a row that shows whether the scene reinforces or challenges the stereotype.

These interpretation are based on my opinions and just research online, so other people may understand a scene differently from me and others. The timestamps I used are a range between when it happened as well.

## Files:

- `initial-dataset.py`: My initial 50 items/dataset I created
- `movies-data.csv`: The dataset csv
- `README.md`: Overview of my topic

## How to Run my Code:

```bash
python3 initial-dataset.py
```

## Future Dataset I will be Adding:

I plan to audit add movies from this github repo [Gender Equality in Movies dataset](https://github.com/melihkurtaran/DIE_Gender_Equality_in_Movies). It contains CSV files with movie dialogues, character genders, and its release year.

I will be exploring how the dataset represents gender stereotyping and what information may be missing and needs cleaning.