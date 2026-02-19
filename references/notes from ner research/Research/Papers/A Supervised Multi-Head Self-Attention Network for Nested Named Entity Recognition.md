---
title: A Supervised Multi-Head Self-Attention Network for Nested Named Entity Recognition
authors: Xu, Y., Huang, H., Feng, C., & Hu, Y
url: https://doi.org/10.1609/aaai.v35i16.17669
keywords: Information Extraction
date: 2021 May 18
---

# key take-aways
Nested NER, Self-Attention, Entity Boundary Detection, Entity Classification, Multi-Class, SMHSA

# description 
## goal
To present neural model for NER treated as multi-class classification of word pairs.
## problem
Previously most existing models ignored the semantinc correlation between words under different entity types.

Previous solutions:
1) Converting nested structures into flat structures such as Hypergraphs or Constituency Trees 
	- drwabacks: 
		- a lot human effort needed for designing unambiguous hypergraph
		- usually hypergraphs designed for nested NER, not suitable for flat NER
2) Sequence-labeling models
	- advantages:
		- achieved good performance on nested NER
	- drawbacks:
		- most of them need extra annotation and complex feature engineering
3) Span-based models
	- drawbacks:
		- learning span representation in computionally expensive
		- classifying spans ignore the explicit boundary information
4) Boundary-aware neural models
	- drawbacks:
		- ignore the relevance between head and tail entities
		- rely on span representation ignoring the correlation between entity spans and entity types which leads to error propagation and redundant information
## solution
Multi-task learning model using supervised, multi-head, self-attention neural method.
- modules: 
	- entity boundary detection (word-level multi-class classification task)
	- entity classification (word-pair-level multi-class classification task)
## dataset
1) Nested NER
	- [[ACE 2004]]
	- [[ACE 2005]]
	- [[GENIA]]
2) Flat NER
	- [[JNLPBA]]
	- [[CoNLL-2003]] - English
## model
- [Source Code](https://github.com/xyxAda/Attention_NER)

## evaluation
- a predicted entity is considered correct only when its span and type match with the gold entity
- precision, recall, micro F1 scores

### references
- [[Neural Architectures for Named Entity Recognition]]
- [Nested Named Entity Recognition](https://aclanthology.org/D09-1015) "One representative category is based on the sequence labeling that convert the nested structures into flat structures by various transform operations, such as construct a syntactic constituency tree ..."
- [Semi-supervised sequence modeling with cross-view training](https://arxiv.org/abs/1809.08370) "One representative category is based on the sequence labeling that convert the nested structures into flat structures by various transform operations, such as (...) build hyper-graphs"
