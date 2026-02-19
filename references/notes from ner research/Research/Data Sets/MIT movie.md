---
title: MIT movie
authors: 
released: 
languages: 
description: 
avaiability: https://huggingface.co/datasets/tner/mit_movie_trivia
tasks: flat NER, movie
tagging schemes:
  - IOB
named entities: Actor, Plot, Opinion, Award, Year, Genre, Origin, Director, Soundtrack, Relationship, Character_Name, Quote
---
## Notes
dostępne na kagglu i hugging-face

## Data structure
- example:
	{
    'tags': [0, 13, 14, 0, 0, 0, 3, 4, 4, 4, 4, 4, 4, 4, 4],
    'tokens': ['a', 'steven', 'spielberg', 'film', 'featuring', 'a', 'bluff', 'called', 'devil', 's', 'tower', 'and', 'a', 'spectacular', 'mothership']
	}