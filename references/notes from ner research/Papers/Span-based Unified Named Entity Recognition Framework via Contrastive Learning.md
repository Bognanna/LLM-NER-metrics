---
title: Span-based Unified Named Entity Recognition Framework via Contrastive Learning
authors: Mao, Hongli and Mao, Xian-Ling and Tang, Hanlin and Shang, Yu-Ming and Gao, Xiaoyan and Ma, Ao-Jie and Huang, Heyan
url: https://doi.org/10.24963/ijcai.2024/708
keywords: Named entities, Information extraction
date: 2024 August
---

# key take-aways
[[Span Based]], Unified NER
# description 
## goal
Propose a novel Span-based Unified NER framework via contrastive learning (SUNER), which aligns text span and entity type representations in a shared semantic space.
## problem
Traditional NER are designed to domain-specific datasets and limited to fixed predifined types = difficulty generalizing to new domains. Promt-based generative methods cannot directly model entity span and suffer from slow sequentioal decoding due to autoregressive structure.
## solution
1) Utilize contrastive learning to enhance model generalizability and propose SUNER, which can jointly handle multiple NER datasets:
	- directly align text spans and entity type representations within a shared semantic space,
	- utilize pretrained language models that have learned general liguistic patterns from large unlabeled corpora.
2) Two modules:
	- span detection - well-designed entity marker, that captures iner-entity relationships while retaining original textual structure
	- span classification
## dataset
1) Flat
	- [[CoNLL-2003]]
	- [[OntoNotes]]
	- [[MIT restaurant]]
	- [[MIT movie]]
2) Nested
	- [[GENIA]]
	- [[ACE 2004]]
	- [[ACE 2005]]
## model
not found

## evaluation
- a predicted entity is considered correct only when its label and boundaries exactly match the ground truth
- precision, recall, F1 scores

# critique

# references
[[Unified Named Entity Recognition as Word-Word Relation Classification]]