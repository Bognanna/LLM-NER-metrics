In this chapter, we propose a novel metric, CDEF, which comprises two measures: CDE (cosinus distance of embeddings) and EF (entities found). First, we discuss the three conditions that we believe the metric should satisfy. We then present the CDE and EF measures. Finally, we introduce the CDEF metric as a combination of these two measures. We then proceed to summarise the conditions to which reference is made at the commencement of the chapter.

The creation of the metric system was predicated on three fundamental conditions. 
1. The metric should be accurate, which means that the results it gives should precisely reflect the quality of the extracted named entities. 
2. The metric under consideration should be reducible, which means that it should allow for approximate mapping into traditional metrics. 
3. Finally, the metric should be interpretable, that is to say, it should be straightforward to comprehend and analyse.

The proposed metric is intended to make a comparison between the embedding vectors of entity names. The use of embeddings enables the comparison of the target information of an entity name, as opposed to the direct writing of the entity name, therefore allowing the acceptance of paraphrases. As demonstrated in previous studies, the application of distance measures between embeddings in the context of LLM responses has been shown to yield accurate results, with the consideration of paraphrases being a contributing factor. However, to the best of the author's knowledge, embeddings have not yet been used in the context of NER tasks.

### Cosinus distance of embeddings
CDEF is comprised of two measures. The first of these, the cosine distance of embeddings (CDE), is a measurement of the semantic similarity between reference entities and generated entities. CDE is defined as the arithmetic mean of the cosine distances between the embeddings of reference entities and those of generated entities. The calculation of distance is conducted only between paired entities. In the event of two paired entities having different entity types, the distance between them is set to 2. This means that despite the similarity of the generated entity to the reference entity, if its type classification is incorrect, its distance to the reference entity will be maximal.

Va1, ..., Van - embedding vectors of reference entities names
Vb1, ..., Vbm - embedding vectors of generated entities names

dist = Dc(Va, Vb) if type(a) == type(b), else 2
CDE = SUM(dist)/(COUNT(dist))

A - set of reference entities
B - set of generated entities

The range of values for this measure is <0;2). Where 0 indicates that paired entities are the same. Result close to 0, suggests the existence of lexical differences between paired entities, while the target information is maintained.

## Entities Found

The Entities Found (EF) measure is defined as the proportion of generated entities in relation to the total number of reference entities. The result of the EF measure indicates whether the set of generated entities corresponds precisely to the set of reference entities.

|A| - number of reference entities
|B| - number of generated entities

EF = 2*|B|/(|A|+|B|) - 1

The range of values for this measure is <-1;1>.
- The result value in range <-1; 0) indicates that the number of generated entities is fewer than the reference entities.
- The result value of 0 indicates that the number of reference entities is equal to the number of generated entities.
-  The result value in range (0;1> signifies that the number of generated entities exceeds the number of reference entities.

## CDEF
The CDEF metric integrates CDE and EF measures to ensure reliable results in the assessment of the quality of generated entities. It is necessary to consider these two measures in combination, since CDE alone will not penalise situations where too few or too many entities are generated. On the other hand, EF alone produce unsatisfactory results, as it exclusively prioritises the number of generated entities, irrespective of their quality.

CDEF is defined as the weighted harmonic mean of 1-CDE/2 and 1-absolute value of EF. These transformations are necessary because CDE and EF have different ranges of values. While CDE has its worst value at 2, EF has it at -1 and 1. As CDEF is inspired by the F-beta score metric, there is a beta coefficient that determines how much the CDE measure will be important in comparison to the EF measure. The range of beta values is <0; oo). As the beta coefficient value increases, the influence of the CDE measure on the final result is reduced, while the influence of the EF measure is increased.

CDEF = \[(1+beta^2)\*(1-(CDE)/2) \* (1-abs(EF))] \ \[(beta^2 \* (1-CDE/2)) + (1- abs(EF))]

The range of values for the CDEF metric is <0;1>. The value of 1 is optimal, while 0 is the worst possible outcome.

## Summary

|         | CDE   | exh_CDE | EF     | CDEF  |     |
| ------- | ----- | ------- | ------ | ----- | --- |
| Range   | <0;2) | <0;2)   | <-1;1> | <0;1> |     |
| Optimal | 0     | 0       | 0      | 1     |     |
| Worst   | 2     | 2       | -1; 1  | 0     |     |
In conclusion, the CDEF metric is comprised of two measures. The CDE is designed to capture semantic similarity between generated entities and reference entities. The EF is intended to penalise situations where too many or too few entities are generated.

The CDEF metric satisfies all three conditions that are stated at the beginning of this chapter.
1. The metric is reducible, since its range of values is <0;1> and 1 indicates an optimal solution. The same trait have traditional metrics, including accuracy, precision, recall and the F1 score.
2. The metric is interpretable, insofar as its results are presented in conjunction with the component measures results.
3. The accuracy of the CDEF metric will be demonstrated in the following chapters, which will present the findings on a number of use cases and benchmarks.
