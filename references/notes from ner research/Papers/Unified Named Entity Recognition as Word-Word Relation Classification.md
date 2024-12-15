---
title: Unified Named Entity Recognition as Word-Word Relation Classification
authors: Jingye Li, Hao Fei, Jiang Liu, Shengqiong Wu, Meishan Zhang, Chong Teng, Donghong Ji, Fei Li
url: https://arxiv.org/abs/2112.10070
keywords: 
date: "2022"
---

# key take-aways
Unified NER, W2NER, Great summary

# description 
## goal
Present a novel alternative by modeling the unified NER as word-word relation classification.

## problem
Bottleneck of unified NER (flat + nested + discontinuous), that lies in the modeling of the neighboring relations between entity words.
## solution
W2NER architecture, that resolves the unified NER by effectively modeling both the entity boundary identification as well as the neighboring relations between entity words.
1) Model the neighbour relations between words:
	- Next-Neighboring-Word
	- Tail-Head-Word
2) Model unified NER as a 2D grid of word pairs.
3) Multi-granularity 2D convolutions.
4) Co-predictor to reason word-word relations.
## dataset
Flat NER Datasets:
- [[CoNLL-2003]]
- OntoNotes 5.0
- OntoNotes 4.0
- MSRA
- Weibo
- Resume

Overlapped NER Datasets:
- [[ACE 2004]]
- [[ACE 2005]]
- [[GENIA]]

Discontinuous NER Datasets:
- [[CADEC]]
- [[ShARe 13]]
- [[ShARe 14]]
## model
[W2NER](https://github.com/ljynlp/W2NER)

### references
- [[Neural Architectures for Named Entity Recognition]]
- [[Rethinking Boundaries End-To-End Recognition of Discontinuous Mentions with Pionter Networks]]
- [[A Span-Based Model for Joint Overlapped and Discontiunuous Named Entity Recognition]]
- [[Locate and Label - A Two-stage Indentifier for Nested Named Entity Recognition]]
- [[Discontinuous Named Entity Recognition as Maximal Clique Discovery]]
- [A Unified Generative Framework for Various NER Subtasks](https://aclanthology.org/2021.acl-long.451.pdf) "Recently propose a sequence-to-sequence (Seq2Seq) model to directly generate various entieties, which unfortunately potentially suffers from the decoding efficiency problem and certain common shortages of Seq2Seq architecture e.g. exposure bias."

