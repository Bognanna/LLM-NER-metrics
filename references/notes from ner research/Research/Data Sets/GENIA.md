---
title: GENIA
authors: Jin-Dong Kim
released: 
languages: "\r\rEnglish"
description: The GENIA corpus is the primary collection of biomedical literature compiled and annotated within the scope of the GENIA project. The corpus was created to support the development and evaluation of information extraction and text mining systems for the domain of molecular biology.
avaiability: https://paperswithcode.com/dataset/genia
tasks: nested NER, biomedical
tagging schemes:
  - text
---
## Notes
- downloaded from Huggingface

## Datastructure
- json file
- example: [
			{
				"tokens": [ ],
				"entities": [ {"start": , "end": , "type": , }, ...],
				"relations": {},
				"org_id": ,
				"pos": [ ], 
				"ltokens": [ ],
				"rtokens": [ ]
			}
		]