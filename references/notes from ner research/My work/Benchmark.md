# Schema
Benchmark consists of 3 files: test_similarities.json, test_types.json, test_mix.json, Each file consists of 130 triples. Each triple consists of 3 sets of entities tuples (entity, type): set "A" contains gold entities and gold types, sets "B" and "C" contains entities tuples that are dissimilar from the entites tuples of set "A". The relationship between sets "A", "B" and "C" is as follows: similarity between "A" and "B" is not smaller than similarity between "A" and "C". While entities tuples in "A" are considered as gold, the tuples in "B" are considered as medium quality and the tuples in "C" as poor quality. 
Sets "A", "B" and "C" forms together a triple. Each file consists of 130 triples. Triples are divided into 4 groups, according to number of entities tuples in each set:
- in the triples with IDs 0-39, |A| >= |B| and |A| >= |C|,
- in the triples with IDs40-79, |A| == |B| == |C|,
- in the triples with IDs 80-119 |A| <= |B| and |A| <= |C|,
- triples with IDs 120-129: (|A| >= |B| and |A| <= |C|) or (|A| <= |B| and |A| >= |C|).
The benchmark consist of 3 files. Each file is created to examine behaviour of different aspect of the metric.
- test_similarities.json is used to examine the performance of the metric according to differences between entities - therefore entity types in each set are perseved the same ad golden types.
- test_types.json is used to examine the performance of the metric according to differences between entity types - therefore entities in each set are perseved the same ad golden entities.
- test_mix.json is used to examine the performance of the metric according to differences between entities and differences between entity types.
# Data description
The benchmark was created partialy manually and pariatlly with use of LLM. Part of gold entities comes from CADEC dataset. For these gold enitites, "B" and "C" sets are created manually. The rest of triples is created with the use of model GPT-4o.
All gold entities are of type "ADR" (Adverse Drug Reaction). To examine the performance of the metric for different entity types, for "B" and "C" sets, some of entities is marked as "Drug" type. The rest of entites is also of "ADR" type.



