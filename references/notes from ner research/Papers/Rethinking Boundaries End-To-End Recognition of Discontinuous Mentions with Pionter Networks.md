---
title: Rethinking Boundaries End-To-End Recognition of Discontinuous Mentions with Pionter Networks
authors: Hao Fei, Donghong Ji, Bobo Li, Yijiang Liu, Yafeng Ren, Fei Li
url: https://doi.org/10.1609/aaai.v35i14.17513
keywords: Information Extraction
date: 2021-05-18
---

# key take-aways
Discontinuous NER, Overlapped NER, Flat NER Pointer Networks, Global Information

# description 
## goal
Present a model for discontinuous NER based on pointer networks.

## problem
Many solutions for nested entieties have been depeloped, however reaserch for discontiunuos entities is still very limited. Main problems of discontiunous NER are:
- decoding ambiguities,
- predicting using token-level local feature.
## solution
Model with 3 major merits:
1) Memory-augmented pointer mechanism to enhance mention boundary detection and interactions between the current decision and pior recognized mentions.
2) Enconder-decoder architecture that can linearize the complexity of structure predictions which leads to reduction of search costs.
3) Global Infrmation used to consult all the input and output.
## dataset
- [[CADEC]]
- [[ShARe 13]]
## model
[DisNER-PtrNet](https://github.com/scofield7419/DisNER-PtrNet)

### references
- [[Neural Architectures for Named Entity Recognition]]
- [Combining Spans into Entities: A Neural Two-Stage Approach for Recognizing Discontiguous Entities](https://aclanthology.org/D19-1644/) "Other approaches aim to build more effective inference systems by modeling the structure as a whole graph, e.g. (...) the two-stage method..."
- [An Effective Transition-based Model for Discontinuous NER.]([https://aclanthology.org/2020.acl-main.520](https://aclanthology.org/2020.acl-main.520)  "Other approaches aim to build more effective inference systems by modeling the structure as a whole graph, e.g. (...) the transition system."