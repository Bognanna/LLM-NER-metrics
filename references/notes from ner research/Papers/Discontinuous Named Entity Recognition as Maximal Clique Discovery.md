---
title: Discontinuous Named Entity Recognition as Maximal Clique Discovery
authors: Yucheng Wang, Bowen Yu, Hongsong Zhu, Tingwen Liu, Nan Yu, Limin Sun
url: https://aclanthology.org/2021.acl-long.63/
keywords: 
date: 2021 August
---

# key take-aways
Discontinuous NER, Joint Extraction, Maximal Clique Discovery

# description 
## goal
Solve the problem of exposure bias.
## problem
Combination-based models and transition-based models have problems with exposure bias
- Combination-based: gap between training and inference,
- Transition-based: skewed prediction devites predictions of the follow-up actions.
## solution
Maximal clique discovery based discontinuous model.

1) Construct segment graph for each sentence:
	- node: a segment containded continuous,
	- edge: links two nodes belonging to the same entity
	It is generated respectivelly in one stage with a grid tagging scheme and learned jointly using a novel architecture named Mac.
2) Reformulate NER:
	Non-parametric process of dicovering maximal cliques in the graph and concatenating the spans in each clique.
## dataset
- [[CADEC]]
- [[ShARe 13]]
- [[ShARe 14]]
## model
[Information Extraction](https://github.com/131250208/infextraction)

### references
- [Evaluating the state of the art in disorder recognition and normalization of the clinical narrative](https://pubmed.ncbi.nlm.nih.gov/25147248/) "... While such assumption is valid for most cases, it does not always hold, especially in clinical corpus."
- [TPLinker: Single-stage Joint Extraction of Entities and Relations Through Token Pair Linking](https://aclanthology.org/2020.coling-main.138/) "Our model is motivated by TPLinker, which formulates joint extraction as a token pair linking problem by aligning the boundary tokens of entity pairs."
