---
title: Nested Named Entity Recognition as Latent Lexicalized Constituency Parsing
authors: Chao Lou, Songlin Yang, Kewei Tu
url: https://aclanthology.org/2022.acl-long.428.pdf
keywords: 
date: "2022"
---

# key take-aways
Nested NER, Lexicalized Constituency Trees

# description 
## goal
To obtain the best of two worlds: proposing a probabilistically principled method that enables exact global inference, meanwhile taking entity heads into account.

## problem
Multiple problems with previous approaches to nested NER.
## solution
Lexicalized constituency trees, with constituent annotated by headwords to model nested entities:
- Eisner-Satta algorithm for lexicalized constituency parsing,
- 2-stage strategy: predict an unlabeled tree and label the predicted constituenties,
- head regularization loss to encourage satisfaction of the constraint,
- head-aware labeling loss.
## dataset
- [[ACE 2004]]
- [[ACE 2005]]
- [[GENIA]]
- [[NNE]]
## model
[Nested NER as Latent Lexicalized Parsing](https://github.com/LouChao98/nner_as_parsing)

### references
- [[A Span-Based Model for Joint Overlapped and Discontiunuous Named Entity Recognition]]
- [[Locate and Label - A Two-stage Indentifier for Nested Named Entity Recognition]]
- [Pyramid: A Layered Model for Nested Named Entity Recognition](https://aclanthology.org/2020.acl-main.525.pdf) "To resolve this problem, there are many layer-based methods proposed to recognize entites layer-by-layer in bottom-up or top-down manners. However, they suffer from the error propagation issue due to the cascade decodnig."
- [Nested Named Entity Recognition with Partially-Observed TreeCRFs](https://arxiv.org/abs/2012.08478) "Recently adapt a span-based constituency parser to tackle nested NER, treating annotated entity spans as partially-observed constituency tree and marginalizing latent spans out for training. (...) However, their method does not consider entity heads, which provide important clues for entity mention detection ans entity typing."