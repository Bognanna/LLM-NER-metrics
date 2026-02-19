## Intuition
Assigning a single tag (label) to each token. Based on tagging scheme eg. BIO. Converting nested structures into flat structures by various transform operations.

## Problems
- It is difficult to design one tagging scheme for all NER subtasks. [[Unified Named Entity Recognition as Word-Word Relation Classification]]
- Doesn't work for nested, overlapped or discontinuous NER [[Rethinking Boundaries End-To-End Recognition of Discontinuous Mentions with Pionter Networks]] [[A Span-Based Model for Joint Overlapped and Discontiunuous Named Entity Recognition]] [[Locate and Label - A Two-stage Indentifier for Nested Named Entity Recognition]] [[Discontinuous Named Entity Recognition as Maximal Clique Discovery]]  [[Nested Named Entity Recognition as Latent Lexicalized Constituency Parsing]]
- heavy reliance on task-specific tagging strategies -> highly specialised, limited their adaptability to new datasets and unseen entity types [[TriG-NER - Triplet-Grid Framework for Discontinuous Named Entuty Recognition]] 
- do not fully capture the token-level dependencies critical for recognising scattered entities [[TriG-NER - Triplet-Grid Framework for Discontinuous Named Entuty Recognition]]

## Examples
- [[Neural Architectures for Named Entity Recognition]]
- [[A Supervised Multi-Head Self-Attention Network for Nested Named Entity Recognition]]

