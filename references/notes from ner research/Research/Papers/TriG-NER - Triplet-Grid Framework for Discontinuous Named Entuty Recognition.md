---
title: TriG-NER - Triplet-Grid Framework for Discontinuous Named Entuty Recognition
authors: Rina Carines Cabral, Soyeon Caren Han, Areej Alhassan, Riza Batista-Navarro, Goran Nenadic, Josiah Poon
url: " \rhttps://doi.org/10.48550/arXiv.2411.01839"
keywords: Discontinuous Named Entity Recognition, Medical Named Entity Recognition, Medical Text Mining
date: 2024-11-04
---

# key take-aways
Token-based triplet loss for NER, Grid-based triplet loss using word-pair relationships, Extensive evaluations and qualitative analysis

# description

## goal
To introduce Trig-NER for dicontinuous NER.
## problem
Problems with previous solutions for discontinuous NER:
1) Tagging Schemes 
	- model thightly coupled to specific tagging strategy
	- model lacking generalisability across diverse datasets and unseen entity types
2) Span Based
	- focus on sample-based learning objectives
3) LLMs
	 - LLMs are optimised for next word prediction
	 - LLMs are prone for generating incorrect spans
	 - LLMs are prone for generating incorrect entity boundaries
4) Grid tagging
	- lack of mechanism to differantiate between similar and dissimilar word-pair representations (missclasification of complex scattered entity spans)
	-  constrained by reliance on specific grid tag design and decoding structure
## solution
A triplet-grid framework that laverages token-based triplet loss to learn fine-grained word-pair relationships for DNER.
- Triplet loss at token level instead of traditional triplet loss that operates on sample level. Instead of comparing entire sentences, comparison of word pairs co-ocurring within the same entity. That ensures that word pairs forming an entity are cohesively represented in the learned feature space.
- Grid-based triplet loss. It models word-pair relationships within a flexible grid structure. It enhances the model's ability to capture non-adjecent entity segments.
## dataset
- [[CADEC]]
- [[ShARe 13]]
- [[ShARe 14]]
## model

### references

