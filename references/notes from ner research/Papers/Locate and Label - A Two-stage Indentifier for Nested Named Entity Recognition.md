---
title: "Locate and Label: A Two-stage Indentifier for Nested Named Entity Recognition"
authors: Yongliang Shen, Xinyin Ma, Zeqi Tan, Shuai Zhang, Wen Wang, Weiming Lu
url: https://aclanthology.org/2021.acl-long.216
keywords: 
date: 2021 August
---

# key take-aways
[[Object detection]], Nested NER, Boundary detection, Span classification
# description 
## goal
Propose a 2-stage entity identifier.

## problem
Problems with span-based methods:
- high computation cost,
- ignorance of boundary information,
- under-utilization of the spans that partially match with entities,
- difficulties in long entity recognition
## solution
Insparied by object detection tasks, instead of treating NER as a classification task on span, treat it as a joint task of boundary regression and span classification.

A two-stage entity identifier:
1) Boundary Detection. Generate span proposals by:
	- filtering (contextual and proposals spans) <- reduction of candidates
	- boundary regression on the seed spans to adjust boundaries of span proposals <- quality improvement
2) Span Classification. Label the boundary-adjusted span proposals with the corresponding categories.

Response for span-based methods problems:
- low-quality seed spans are filtered out,
- effective utilization of the boundary information
- effective utilization of partially matched spans during training
- entities of any lenght can be covered
## dataset
- [[ACE 2004]]
- [[ACE 2005]]
- [[KBP 2017]]
- [[GENIA]]
## model
[locate-and-label](https://github.com/tricktreat/locate-and-label)

### references
- [FLAT: Chinese NER Using Flat-Lattice Transformer](https://aclanthology.org/2020.acl-main.611/) "In recent years, several approaches have been proposed to solve the nested named entity recognition task, mainly including tagging-based (...) Pyramid designs a pyramid structured tagging framework that uses CNN networks to identify entities from the bottom up."
- [Named Entity Recognition as Dependency Parsing](https://aclanthology.org/2020.acl-main.577/) "... reformulated NER as a structured prediction task ans adopted a biaffine model for nested and flat NER."
- [A Unified MRC Framework for Named Entity Recognition](https://aclanthology.org/2020.acl-main.519/) "... treated NER as a reading comprehension task, and constructed type-specific queries to extract entities from the context."