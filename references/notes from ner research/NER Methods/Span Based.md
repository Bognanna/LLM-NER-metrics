## Intuition
Enumerate all possible spans and perform span-level classification.

## Problems
- Considerable model complexity [[Unified Named Entity Recognition as Word-Word Relation Classification]]
- Ignorance of boundary information -> innacurate detection of entities boundaries, [[A Supervised Multi-Head Self-Attention Network for Nested Named Entity Recognition]] [[Locate and Label - A Two-stage Indentifier for Nested Named Entity Recognition]]
- Under-utilization of the spans that partially match with entities, [[Locate and Label - A Two-stage Indentifier for Nested Named Entity Recognition]]
- Difficulties in long entity recognition (maximal span lenghts) [[Locate and Label - A Two-stage Indentifier for Nested Named Entity Recognition]] [[Unified Named Entity Recognition as Word-Word Relation Classification]]
- Computationally expensive <- numerous low-quality candidate spans [[A Supervised Multi-Head Self-Attention Network for Nested Named Entity Recognition]] [[Locate and Label - A Two-stage Indentifier for Nested Named Entity Recognition]]

## Examples
- [[A Span-Based Model for Joint Overlapped and Discontiunuous Named Entity Recognition]]
- [[Locate and Label - A Two-stage Indentifier for Nested Named Entity Recognition]]

