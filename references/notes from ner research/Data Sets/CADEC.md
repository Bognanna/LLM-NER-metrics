---
title: CADEC
authors: " Karimi, Sarvnaz , Metke Jimenez, Alejandro , Kemp, Madonna , Wang, Chen"
released: 2016-04-14
languages: "\r\rEnglish"
description: CSIRO Adverse Drug Event Corpus (Cadec) is a rich annotated corpus of medical forum posts on patient reported Adverse Drug Events (ADEs). This corpus is useful for those studies in the area of information extraction, or more generically text mining, from social media to detect possible adverse drug reactions from direct patient reports.
avaiability: https://doi.org/10.4225/08/570FB102BDAD2
tasks: discontinuous NER, biomedical domain
tagging schemes:
  - text, AMT/SCT, MedDRA
---
## Notes
- easy to access
- cadec.v2 contains txt files
- entity types: ADR (Adverse Drug Reaction), Drug, Disease, Symptom, Finding,

## Data structure
#### CADECv1
1) Original -  the entities annotated in the posts
	- format: Tag number | Entity Type | offsets | text
	- example: T1	ADR 9 19	bit drowsy
		#1	AnnotatorNotes T1	Drowsy
2) AMT-SCT - annotated with SCT or AMT concepts.
	- format: Tag number | SCT/AMT concept | Standard terminology | offsets | text
	- example: TT1	271782001 | Drowsy | 9 19	bit drowsy
3) MedDRA - annotated with MedDRA codes in a similar format. 
	- format: Tag number | SCT/AMT concept | offsets | text
	- example: TT1	10013649 9 19	bit drowsy
#### CADECv2
1) Original -  the entities annotated in the posts
	- format: Tag number | Entity Type | offsets | text
	- example: T1	ADR 9 19	bit drowsy
		#1	AnnotatorNotes T1	Drowsy
2) AMT-SCT - annotated with SCT or AMT concepts.
	- format: Tag number | SCT/AMT concept | Standard terminology | offsets | text
	- example: TT1	271782001 | Drowsy | 9 19	bit drowsy
3) MedDRA - annotated with MedDRA codes in a similar format. 
	- format: Tag number | SCT/AMT concept | offsets | text
	- example: TT1	10013649 9 19	bit drowsy
4) **text - orignal text**

