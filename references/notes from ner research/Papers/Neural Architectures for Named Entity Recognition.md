---
title: Neural Architectures for Named Entity Recognition
authors: Guillaume Lample, Miguel Ballesteros, Sandeep Subramanian, Kazuya Kawakami, Chris Dyer
url: https://aclanthology.org/N16-1030
keywords: 
date: 2016 June
---

# key take-aways
[[Sequence Labeling]], BiLSTM, LSTM-CRF, Stack-LSTM, 
Transition-based models, Taggigng Schemes, Flat NER

# description 
## goal
To introduce 2 new neural architectures for NER that use no language-specific resources or features.
## problem
NER is a challenging problem due to two major factors:
- very small amount of supervised train data
- difficult genaralizing:
	- small samples of data
	- "there are few constraints on the kinds of words that can be names" **(?)**

Past solutions:
1) Use datasets from language-specific knowledge resources (e.g. gazetters) and carefully constructed orthografic features
- drawback: costly adaptation to new languages and new domains
2) Unsupervised learning used to augment hand-engineered features
+ advantage: improves generalization
+ drawback: still not sufficient
## solution
Neural architecture that:
- uses no language-specific resources or features
- designed to capture 2 intuitions:
	- multiple name tokens tagged jointly
		- LSTM-CRF (a bidirectional LSTM with a sequential conditional random layer above it)
		- S-LSTM (stack LSTM)
	- token-level evidence for "being a name"
		- Orthographic
		- Distributional
## dataset
- [[CoNLL-2002]]
- [[CoNLL-2003]]
## model
- [NER Tagger](https://github.com/glample/tagger)
- [Transition-based NER system](https://github.com/clab/stack-lstm-ner)
- [...](https://paperswithcode.com/paper/neural-architectures-for-named-entity)

### references
- [Finding Function in Form: Compositional Character Models for Open Vocabulary Word Representation](https://arxiv.org/abs/1508.02096) "To capture orthografic sensitivity, we use character-based word representation model ..."
- [Distributed Representations of Words and Phrases and their Compositionality](https://proceedings.neurips.cc/paper/2013/hash/9aa42b31882ec039965f3c4923ce901b-Abstract.html) "(...) to capture distributional sensitivity, we combine these (character-based) representations with distributional representations."

