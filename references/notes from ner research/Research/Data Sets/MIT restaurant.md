---
title: MIT restaurant
authors: 
released: 
languages: 
description: 
avaiability: https://huggingface.co/datasets/tner/mit_restaurant
tasks: flat NER, restaurant
tagging schemes:
  - IOB
named entities: Rating, Amenity, Location, Restaurant_Name, Price, Hours, Dish, Cuisine
---
## Notes
dostępne na kagglu i hugging-face

## Data structure
- example:
	{
    'tags': [0, 0, 0, 0, 0, 0, 0, 0, 5, 3, 4, 0],
    'tokens': ['can', 'you', 'find', 'the', 'phone', 'number', 'for', 'the', 'closest', 'family', 'style', 'restaurant']
	}