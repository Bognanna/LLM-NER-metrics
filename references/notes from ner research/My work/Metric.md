
*The new metric should satisfy the following conditions:*  
- *Accuracy: The metric should precisely reflect the quality of named entity extraction.*  
- *Reducibility: The metric should allow for approximate mapping (projection) onto traditional metrics.*  
- *Interpretability: The metric should be easy to understand and interpret.*

The metric comprises of two measures: Cosinus Distance of Embeddings (CDE) and Entities Found (EF).

## Cosinus Distance of Embeddings

CDE is the arthmetical average of cosinus distances between the embeddings of gold entities and the embeddings of generated entities. The distance is calculated only for paired entites. If two paired entites have different enitiy types, the distance between them is set to 1. CDE is dependent on the method of pairing the generated and gold entities.

Va1, ..., Van - embedding vectors of gold entities
Vb1, ..., Vbm - embedding vectors of generated entities

dist = Dc(Va, Vb) if type(a) == type(b), else 1
CDE = SUM(dist)/(COUNT(dist) + epsilon)

A - set of gold entities
B - set of generated entities

The greedy pairing method:
(1) From sets A, B choose such entities a and b for which dist(Va,Xb) is the smallest.
(2) Remove a, b from A and B.
(3) If A or B is empty: calculate CDE.
Otherwise: return to (1)

The exhaustive pairing method:
(1) For every possible combination of pairs between sets A, B calculate CDE.
(2) Choose combination with the smallest CDE.

The range of values for this measure is <0;2). Where 0 indicates that paired entities are the same.

## Entities Found

EF shows the proportion between number of generated entities and number of gold enitites.

|A| - number of gold entities
|B| - number of generated entities

EF = 2*|B|/(|A|+|B|) - 1

The range of values for this measure is <-1;1>:
- <-1; 0) indicated that there are less generated entities than gold entities
- 0 indicates that there is the same number of gold entities as generated entities
- (0;1> indicates that ther are more generated entities than gold entities

## CDEF
CDEF is the weighted harmonic mean of CDE/2 and absolute value of EF. 

*CDEF = (1+beta^2)\*(CDE)/2 \* abs(EF)) \ \[(beta^2 \* CDE/2) + abs(EF) + epsilon]*

*The range of values for this metric is <0;1>.*
*(!sic) if EF=0 or CDE=0, then CDEF=0, no matter how the rest of measures look like !!!*

CDEF = (1+beta^2)\*1-(CDE)/2 \* 1-abs(EF)) \ \[(beta^2 \* 1-CDE/2) + 1- abs(EF)]

The range of values for this metric is <0;1>. Where 1 is the optimal value and 0 is the worst.

Epsilon is not needed, because b cannot equal 0 (it would indicate, that there are no gold or generated entities).



