
12.  **Benchamark tests** Testy na Benchmarku
	1. **Benchmark description** Przedstawienie Benchmarku
		1. **Schema** Schemat
		2. **Data** Pochodzenie danych: CADEC + GPT-4o + praca manualna
	2. **Tests** Opis przebiegu testów
	3. **Conclusions** Wnioski z testów


Benchmark consists of 3 files: test_similarities.json, test_types.json, test_mix.json, Each file consists of 130 triples. Each triple consists of 3 sets of entities tuples (entity, type): set "A" contains gold entities and gold types, sets "B" and "C" contains entities tuples that are dissimilar from the entites tuples of set "A". The relationship between sets "A", "B" and "C" is as follows: similarity between "A" and "B" is not smaller than similarity between "A" and "C". While entities tuples in "A" are considered as gold, the tuples in "B" are considered as medium quality and the tuples in "C" as poor quality. 
Sets "A", "B" and "C" forms together a triple. Each file consists of 130 triples. Triples are divided into 4 groups, according to number of entities tuples in each set:
- in the triples with IDs 0-39, |A| >= |B| and |B| >= |C|,
- in the triples with IDs40-79, |A| == |B| == |C|,
- in the triples with IDs 80-119 |A| <= |B| and |B| <= |C|,
- triples with IDs 120-129: (|A| >= |B| and |B| <= |C|) or (|A| <= |B| and |B| >= |C|).
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

## Results

In tables are presented results from benchmark tests. In the column "Passed" there is an information how many tests out of 130 passed, the column "Failed" contains information about how many  tests out of 130 failed. Columns 0-39, 40-79, 80-119, 120-129 presents how many failures occured among particular groups of test cases, the numbers in the names of this columns reflects the ids of test cases.

The test case is considered as passed if the measures or metrics value for A and B is closer or equal distance to optimal than between A and C.

Each row represents how particular measure or metric performed on the benchmark. The comparison is made between CDE measure, EF measure and CDEF metric with different beta scores.

Tests on mix benchmark reflect the real world case scenarios, where tags could be mismatched and generated enitites can differ from the gold entities. 
Tests on similarities and tests on types show how measures and metrics behavies in component scenarios.

There can be observed that CDE and EF measures have problems in different types of test cases.

CDE mostly struggles with test cases 0-39, where |A| >= |B| and |B| >= |C|. It is expected behaviour, that can be explained by following example:
`{"A": [["puppy", "animal"], ["kitten", "animal"], ["chick", "animal"]], "B":  [["dog", "animal"], ["kitten", "animal"], ["chick", "animal"]], "C": [["kitten", "animal"]]}`
There B captures all enitites, however instead of "puppy" there is similar phrase "dog". The CDE metric, calculates the average distance which is close to 0, but not equal 0, since between "dog" and "puppy" there is a small, not 0 distance. 
The C captures only one entitiy, however it is exact as in A, so the average distance calculated by CDE should equal 0. 
For this example CDE idicates that distance between A nad C is closer than A and B.

The EF measure fail in cases 120-129, since there the numbed of enitites betwen A, B and C is neither nondecreasing nor nonincreasing. EF is very primitive measure, thats only purpose is to correct the problem with CED measure described above.

The CDEF metric as a combination of EF and CDE. The greater is the beta value, the stronger influence of EF is on the result. For beta=0.0, there is no influence of EF on the result, therefore metric fail on the same test cases as CDE measure. With the increase of beta value, there are more failures characteristic for EF and less failures characteristic for CDE. The optimal value of beta is different for every scenario: for test similaritis it is around 0.5 and for test mix is around 1.5.

### test similarities

| Metric    | Passed | Failed | 0-39 | 40-79 | 80-119 | 120-129 |
| --------- | ------ | ------ | ---- | ----- | ------ | ------- |
| CDE       | 112    | 18     | 11   | 4     | 3      | 0       |
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

### test types

| Metric    | Passed | Failed | 0-39 | 40-79 | 80-119 | 120-129 |
| --------- | ------ | ------ | ---- | ----- | ------ | ------- |
| CDE       | 130    | 0      | 0    | 0     | 0      | 0       |
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

### Conclusions
CDEF metric behavies accurately in 127 out of 130 benchamrk use cases for mix benchmark. This can be considered as a very good result, that shows that this metric works. In this dataset it is also visible why CDE and EF need to be combined together, in order to reflect as good as possible the real quality of generated enitites.