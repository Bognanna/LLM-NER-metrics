---
title: A Span-Based Model for Joint Overlapped and Discontiunuous Named Entity Recognition
authors: Fei Li, ZhiChao Lin, Meishan Zhang, Donghong Ji
url: https://aclanthology.org/2021.acl-long.372
keywords: 
date: 2021 August
---

# key take-aways
[[Span Based]], Overlapped NER, Discontinuous NER
# description 
## goal
Propose a novel span-based model that can recognize both overlapped and discontinuous entities jointly.
## problem
Previously solutions for either overlapped or  discontinuous entities. Challenge to recognize them jointly.
## solution
1) Recognition of overlapped entities:
	- enumerate all possible text spans in a sentence
	- exploit a multi-classification strategy
2) Recognition of relationships between entity fragments:
	- pairwise relation classification over all entities (succesion, overlaping, other)
## dataset
1) Overlapped + discontinuous
	- [[ShARe 13]]/CLEF
	- [[CADEC]]
2) Overlapped
	- [[GENIA]]
	- [[ACE 2005]]
## model
[A Span-Based Model for Joint Overlapped and Discontinuous Named Entity Recognition](https://github.com/foxlf823/sodner)

## evaluation
- a predicted entity is considered correct only when its span and type match with the gold entity
- for a discontinuous entity: each span should match a span of the gold entity
- precision, recall, F1 scores

# critique
- problems with maximal span lengths [[Unified Named Entity Recognition as Word-Word Relation Classification]]
- considerable model complexity due to the enumerating nature [[Unified Named Entity Recognition as Word-Word Relation Classification]]
- suffer from heavy reliance on task-specific tagging strategies [[TriG-NER - Triplet-Grid Framework for Discontinuous Named Entuty Recognition]]:
	- highly specialized (limited adaptability to new datasets and unseen entity types)
# references
- [[Neural Architectures for Named Entity Recognition]]
- [Learning to Recognize Discontiguous Entities](https://arxiv.org/abs/1810.08579) "The hypergraph (...) models are flexible to be adapted for different tasks, achievieng great successes for overlaped or discontinuous NER."
- [Neural Segmental Hypergraphs for Overlapping Mention Recognition](https://arxiv.org/abs/1810.01817) "The hypergraph (...) models are flexible to be adapted for different tasks, achievieng great successes for overlaped or discontinuous NER."
- [A General Framework for Information Extraction using Dynamic Span Graphs](https://arxiv.org/abs/1904.03296) "Recently utilized the span-based model for information extraction effectively."