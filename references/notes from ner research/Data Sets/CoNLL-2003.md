---
title: CoNLL-2003
authors: "Tjong Kim Sang, Erik F. and\r De Meulder, Fien"
released: "2003"
languages: "\r\rEnglish, German"
description: "The shared task of CoNLL-2003 concerns language-independent named entity recognition. We will concentrate on\rfour types of named entities: persons, locations, organizations and names of miscellaneous entities that do\rnot belong to the previous three groups."
avaiability: https://paperswithcode.com/dataset/conll-2003
tasks: flat NER
tagging schemes:
  - IOB2
named entities: persons, locations, organizations, miscellaneous
---
## Notes
- downloaded via Kaggle

## Data structure
- format: word | POS tag | syntatic chunk tag | named entity tag
- example: EU NNP B-NP B-ORG
		rejects VBZ B-VP O
		German JJ B-NP B-MISC
