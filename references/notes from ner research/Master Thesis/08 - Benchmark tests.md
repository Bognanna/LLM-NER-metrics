
12.  **Benchamark tests** Testy na Benchmarku
	1. **Benchmark description** Przedstawienie Benchmarku
		1. **Schema** Schemat
		2. **Data** Pochodzenie danych: CADEC + GPT-4o + praca manualna
	2. **Tests** Opis przebiegu testów
	3. **Conclusions** Wnioski z testów


Benchmark consists of 3 files: test_similarities.json, test_types.json, test_mix.json, Each file consists of 130 triples. Each triple consists of 3 sets of entities tuples (entity, type): set "A" contains gold entities and gold types, sets "B" and "C" contains entities tuples that are dissimilar from the entites tuples of set "A". The relationship between sets "A", "B" and "C" is as follows: similarity between "A" and "B" is not smaller than similarity between "A" and "C". While entities tuples in "A" are considered as gold, the tuples in "B" are considered as medium quality and the tuples in "C" as poor quality. 
Sets "A", "B" and "C" forms together a triple. Each file consists of 130 triples. Triples are divided into 4 groups, according to number of entities tuples in each set:
- in the triples with IDs 0-39, |A| >= |B| and |A| >= |C|,
- in the triples with IDs40-79, |A| == |B| == |C|,
- in the triples with IDs 80-119 |A| <= |B| and |A| <= |C|,
- triples with IDs 120-129: (|A| >= |B| and |A| <= |C|) or (|A| <= |B| and |A| >= |C|).
The benchmark consist of 3 files. Each file is created to examine behaviour of different aspect of the metric.
- test_similarities.json is used to examine the performance of the metric according to differences between entities - therefore entity types in each set are perseved the same ad golden types.
- `{"A": [["decreased testosterone", "ADR"], ["decreased libido", "ADR"]], "B": [["decreased testosterone", "ADR"], ["libido", "ADR"]], "C": [["decreased testosterone and libido", "ADR"]], "ID": 0},

        {"A": [["muscle pain", "ADR"], ["joint pain", "ADR"]], "B": [["muscle", "ADR"], ["joint pain", "ADR"]], "C": [["muscle/joint pain", "ADR"]], "ID": 1},

        {"A": [["increased blood pressure", "ADR"], ["increased heart rate", "ADR"]], "B": [["blood pressure", "ADR"], ["heart rate", "ADR"]], "C": [["increased blood pressure and heart rate", "ADR"]], "ID": 2}
- test_types.json is used to examine the performance of the metric according to differences between entity types - therefore entities in each set are perseved the same as gold entities.
- `{"A": [["decreased testosterone", "ADR"], ["decreased libido", "ADR"]], "B": [["decreased testosterone", "Drug"], ["decreased libido", "ADR"]], "C": [["decreased testosterone", "Drug"]], "ID": 0},

        {"A": [["muscle pain", "ADR"], ["joint pain", "ADR"]], "B": [["muscle pain", "Drug"], ["joint pain", "ADR"]], "C": [["muscle pain", "Drug"]], "ID": 1},

        {"A": [["increased blood pressure", "ADR"], ["increased heart rate", "ADR"]], "B": [["increased blood pressure", "Drug"], ["increased heart rate", "ADR"]], "C": [["increased blood pressure", "Drug"]], "ID": 2},
- test_mix.json is used to examine the performance of the metric according to differences between entities and differences between entity types.
- `{"A": [["decreased testosterone", "ADR"], ["decreased libido", "ADR"]], "B": [["decreased testosterone", "ADR"], ["libido", "Drug"]], "C": [["decreased testosterone and libido", "ADR"]], "ID": 0},

        {"A": [["muscle pain", "ADR"], ["joint pain", "ADR"]], "B": [["muscle", "ADR"], ["joint pain", "ADR"]], "C": [["muscle/joint pain", "Drug"]], "ID": 1},

        {"A": [["increased blood pressure", "ADR"], ["increased heart rate", "ADR"]], "B": [["blood pressure", "ADR"], ["heart rate", "ADR"]], "C": [["increased blood pressure and heart rate", "ADR"]], "ID": 2},

### test similarities

| Metric    | Passed | Failed | 0-39 | 40-79 | 80-119 | 120-129 |
| --------- | ------ | ------ | ---- | ----- | ------ | ------- |
| CDE       | 112    | 18     | 11   | 4     | 3      | 0       |
| exh_CDE   | 112    | 18     | 11   | 4     | 3      | 0       |
| EF        | 121    | 9      | 0    | 0     | 0      | 9       |
| CDEF-0.0  | 112    | 18     | 11   | 4     | 3      | 0       |
| CDEF-0.25 | 119    | 11     | 4    | 4     | 2      | 1       |
| CDEF-0.5  | 120    | 10     | 0    | 4     | 0      | 6       |
| CDEF-0.75 | 117    | 13     | 0    | 4     | 0      | 9       |
| CDEF-1.0  | 117    | 13     | 0    | 4     | 0      | 9       |
| CDEF-1.25 | 117    | 13     | 0    | 4     | 0      | 9       |
| CDEF-1.5  | 117    | 13     | 0    | 4     | 0      | 9       |
| CDEF-1.75 | 117    | 13     | 0    | 4     | 0      | 9       |
| CDEF-2.0  | 117    | 13     | 0    | 4     | 0      | 9       |
| CDEF-0.36 | 121    | 9      | 1    | 4     | 0      | 4       |

### test types

| Metric    | Passed | Failed | 0-39 | 40-79 | 80-119 | 120-129 |
| --------- | ------ | ------ | ---- | ----- | ------ | ------- |
| CDE       | 130    | 0      | 0    | 0     | 0      | 0       |
| exh_CDE   | 130    | 0      | 0    | 0     | 0      | 0       |
| EF        | 121    | 9      | 0    | 0     | 0      | 9       |
| CDEF-0.0  | 130    | 0      | 0    | 0     | 0      | 0       |
| CDEF-0.25 | 130    | 0      | 0    | 0     | 0      | 0       |
| CDEF-0.5  | 130    | 0      | 0    | 0     | 0      | 0       |
| CDEF-0.75 | 130    | 0      | 0    | 0     | 0      | 0       |
| CDEF-1.0  | 130    | 0      | 0    | 0     | 0      | 0       |
| CDEF-1.25 | 130    | 0      | 0    | 0     | 0      | 0       |
| CDEF-1.5  | 130    | 0      | 0    | 0     | 0      | 0       |
| CDEF-1.75 | 130    | 0      | 0    | 0     | 0      | 0       |
| CDEF-2.0  | 130    | 0      | 0    | 0     | 0      | 0       |

### test mix

| Metric    | Passed | Failed | 0-39 | 40-79 | 80-119 | 120-129 |
| --------- | ------ | ------ | ---- | ----- | ------ | ------- |
| CDE       | 108    | 22     | 18   | 3     | 1      | 0       |
| exh_CDE   | 108    | 22     | 18   | 3     | 1      | 0       |
| EF        | 120    | 10     | 0    | 0     | 4      | 6       |
| CDEF-0.0  | 108    | 22     | 18   | 3     | 1      | 0       |
| CDEF-0.25 | 109    | 21     | 17   | 3     | 1      | 0       |
| CDEF-0.5  | 112    | 18     | 15   | 3     | 0      | 0       |
| CDEF-0.75 | 112    | 18     | 15   | 3     | 0      | 0       |
| CDEF-1.0  | 112    | 18     | 15   | 3     | 0      | 0       |
| CDEF-1.25 | 112    | 18     | 15   | 3     | 0      | 0       |
| CDEF-1.5  | 127    | 3      | 0    | 3     | 0      | 0       |
| CDEF-1.75 | 126    | 4      | 0    | 3     | 0      | 1       |
| CDEF-2.0  | 126    | 4      | 0    | 3     | 0      | 1       |
