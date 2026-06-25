In this chapter, we present a novel metric called CDEF, comprising two measures: CDE (cosinus distance of embeddings) and EF (entities found). First, we discuss the three conditions that we believe the metric should satisfy. We then present the CDE and EF measures. Finally, we introduce the CDEF metric as a combination of these two measures. We then summarize the conditions referred to at the beginning of the chapter.

At the beginnig of the process of creting metric we set 3 conditions. The metric should be accurate, which means that the results it gives should precisely reflect the quality of extracted named entities. The metric should be reducible, which means that it should allow for approximate mapping into traditional metrics. Last, but not least it should be interpretable, so it should be easy to understand and interpret.

The metric I present compares embedding vectors of entities. It allows for comparing the meaning of the entites, accepting the paraprhases. Previously authors of BERTscore and MoverScore showed that in case of LLM responses, using distance between embeddings can give accurate results, that having in mind paraphrases.

### Cosinus distance of embeddings
The first of two measures is CDE, which stands for Cosinus Distance of Embeddings. It measures the semantically similaritty between gold enitites and generated entities. CDE is the arthmetical average of cosinus distances between the embeddings of gold entities and the embeddings of generated entities. The distance is calculated only for paired entites. If two paired entites have different enitiy types, the distance between them is set to 2. That means that despite the similarity of generated entity to gold entity, if its will be classified as a wrong type of entity, its distance to gold entity will be maximal.

Va1, ..., Van - embedding vectors of gold entities
Vb1, ..., Vbm - embedding vectors of generated entities

dist = Dc(Va, Vb) if type(a) == type(b), else 1
CDE = SUM(dist)/(COUNT(dist))

A - set of gold entities
B - set of generated entities

The range of values for this measure is <0;2). Where 0 indicates that paired entities are lexicaly the same. Results close to 0 indicate that there are some lexical differences between paired enitites, however semantically they are close.

### How to match entities into pairs?


## Entities Found

EF stands for Enitites Found measure and it reflects the proportion between number of generated entities and number of gold enitites. It shows weather the set of generated enitites has exact number of entites as set of gold enitites.

|A| - number of gold entities
|B| - number of generated entities

EF = 2*|B|/(|A|+|B|) - 1

The range of values for this measure is <-1;1>:
- <-1; 0) indicated that there are less generated entities than gold entities
- 0 indicates that there is the same number of gold entities as generated entities
- (0;1> indicates that ther are more generated entities than gold entities

## CDEF
CDEF mereges CDE and EF measures together in order to give trustfull results determining the quality of generated enitites. It is necessary to comprise these two measures, beacuse CDE alone will not penalitaze situations where too little or too many enitites is generated. From the other hand, EF alone gives very poor results, because it only focuses on number of generated enitites, no matter their quality.

CDEF is the weighted harmonic mean of 1-CDE/2 and 1-absolute value of EF. These transformations are necessary, because CDE and EF has different ranges of values and while CDE its worst value in 2, EF has it in -1 and 1. As CDEF is inspired by the F-beta score metric, there is a beta coefficient, that determinies how much CDE measure will be important in favour of EF measure. The range of beta value is <0; oo). If beta <1, then the CDE has greater impact on the final result than EF, for beta=1, CDE and EF are both treated the same, for beta >1, EF has more impact on the final result than CDE.

CDEF = \[(1+beta^2)\*(1-(CDE)/2) \* (1-abs(EF))] \ \[(beta^2 \* (1-CDE/2)) + (1- abs(EF))]

The range of values for this metric is <0;1>. Where 1 is the optimal value and 0 is the worst.

## Summary

|         | CDE   | exh_CDE | EF     | CDEF  |
| ------- | ----- | ------- | ------ | ----- |
| Range   | <0;2) | <0;2)   | <-1;1> | <0;1> |
| Optimal | 0     | 0       | 0      | 1     |
| Worst   | 2     | 2       | -1; 1  | 0     |
Concluding this chapter, the CDEF metric comprises two measures: CDE that captures semantic similarity between generated entites and gold enitites, and EF that penalitizes situations, where too many or too little enitites are generated. CDEF same as traditional metrics such us Accuracy, Precission, Recall, F1-score , has its range of values in <0;1>, where 1 indicated optimal solution. That makes this metric reducable. The metric is also interpretable, as far as its results are presented together with component measures results.
In following chapters I show on several benchmarks and use cases that CDEF metric is also accurate. 