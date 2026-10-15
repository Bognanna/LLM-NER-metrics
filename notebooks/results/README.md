# Results directory

## Directory structure
├───benchmark               # Results of running tests on benchmark datasets. For each embedding model results are stored in separate directories.
│   ├───embeddinggemma      # Results of running tests with the embeddinggemma model.
│   │   ├───detailed            # Detailed results stored in 3 csv files, each for one dataset.
│   │   └───summary             # Tests results stored in 3 csv files, each for one dataset.
│   ├───granite-embedding   # Results of running tests with the granite-embedding model.
│   │   ├───detailed            # ----||----
│   │   └───summary
│   ├───mxbai-embed-large   # Results of running tests with the mxbai-embed-large model.
│   │   ├───detailed            # ----||----
│   │   └───summary
│   ├───nomic-embed-text    # Results of running tests with the nomic-embed-text model.
│   │   ├───detailed            # ----||----
│   │   └───summary
│   ├───qwen3-embedding     # Results of running tests with the qwen3-embedding model.
│   │   ├───detailed            # ----||----
│   │   └───summary
│   └───snowflake-arctic-embed  # Results of running tests with the snowflake-arctic-embed model.
│       ├───detailed            # ----||----
│       └───summary
└───use cases               # Results of running tests on use cases. Each use case file contains results for all tested embedding models.

## Files structure

### Benchmark/embed-model
Results of running tests on the benchmark datasets are stored in separate directories for each embedding model used.

#### detailed

##### Sample
```
,test_id,lists,cde,exh_cde,ef,cdef_0.0,cdef_0.25,cdef_0.5,cdef_0.75,cdef_1.0,cdef_1.25,cdef_1.5,cdef_1.75,cdef_2.0
0,0,AB,1.0,1.0,0.0,0.5,0.5151515151515151,0.5555555555555556,0.6097560975609756,0.6666666666666666,0.7192982456140351,0.7647058823529411,0.8024691358024691,0.8333333333333334
1,0,AC,0.10083499237256766,0.10083499237256766,-0.33333333333333337,0.9495825038137162,0.9264552511985299,0.8752922886372656,0.823736525166441,0.7833631275483598,0.7543766248427771,0.7339500289831576,0.7194283612558172,0.7089087043509732
2,1,AB,0.11240843544946805,0.11240843544946805,0.0,0.943795782275266,0.9469264446319365,0.9545254535583853,0.9632864564989129,0.9710853278738235,0.9772882970478968,0.9820062465837568,0.9855530061379736,0.9882299346003689
3,1,AC,2.0,2.0,-0.33333333333333337,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0
...
```

##### Column description
` ` (int) - row ID
`test_id` (int) - test ID, respective to the ids stored in benchmark datasets
`lists` (str) {AB, AC} - names of 2 lists for which metrics were calculated. Test is passed if result for `AB` indicates greater or the same similarity as result for `AC`.
`cde` (float64) - results of the CDE measure with the greedy approach to pair entities
`exh_cde` (float64) - results of the CDE measure with exhaustive approach to pair entities, they should be the same as for CDE with the greedy approach
`ef` (float64) - results of the EF measure
`cdef_0.0` (float64) - results of the CDEF metric with beta = 0, they should be the same as for CDE
`cdef_0.25` (float64) - results of the CDEF metric with beta = 0.25
`cdef_0.5` (float64) - results of the CDEF metric with beta = 0.5
`cdef_0.75` (float64) - results of the CDEF metric with beta = 0.75
`cdef_1.0` (float64) - results of the CDEF metric with beta = 1
`cdef_1.25` (float64) - results of the CDEF metric with beta = 1.25
`cdef_1.5` (float64) - results of the CDEF metric with beta = 1.5
`cdef_1.75` (float64) - results of the CDEF metric with beta = 1.75
`cdef_2.0` (float64) - results of the CDEF metric with beta = 2


#### summary

##### Sample
```
Benchmark,Metric,Passed,Failed,0-39,40-79,80-119,120-129,
MIX,CDE,104,26,21,3,2,0,
MIX,exh_CDE,104,26,21,3,2,0,
MIX,EF,120,10,0,0,0,10,
MIX,CDEF-0.0,104,26,21,3,2,0,
...
```
##### Column description
`Benchmark` (str) {MIX, SIM, TYPE} - name of benchmark dataset file for which tests were run
`Metric` (str) {CDE, exh_CDE, EF, CDEF-beta} - name of metric for which tests were run
`Passed` (int) {<=130} - number of tests which passed (tests, where score for lists AB was equal or better than for AC)
`Failed` (int) {<=130} - number of tests that failed
`0-39` (int) {<=40} - number of tests with ids 0-39 that failed, these tests are of the type |A| <= |B| <= |C|
`40-79` (int) {<=40} - number of tests with ids 40-79 that failed, these tests are of the type |A| == |B| == |C|
`80-119` (int) {<=40} - number of tests with ids 80-119 that failed, these tests are of the type |A| => |B| => |C|
`120-129` (int) {<=10} - number of tests with ids 120-129 that failed, these tests are of the other type

### use cases
Results of running tests on the use cases are stored in separate files for each use case.

#### uc_description.txt
```
uc11    # use case ID
sentence = "The patient reported pain in the lower back and occasionally in the right leg." # Sentence
gold_entities = [
    ['pain in the lower back', 'Symptom'],
    ['pain in the right leg', 'Symptom']
] # Ground truth entities for the sentence
generated_entities_1 = [
    ['pain', 'Symptom'], ['lower back', 'Symptom'], ['right leg', 'Symptom']
]   # List of generated entities for the sentence
generated_entities_2 = [
    ['pain in the lower back', 'Symptom'], ['occasionally in the right leg pain', 'Symptom']
]   # List of generated entities for the sentence
```

#### ucX.txt

##### Sample
```
model, ent_group, cde, ef, cdef_05, cdef_1
nomic-embed-text, 1, 0.12165669005639607, 0.19999999999999996, 0.9075938214291815, 0.8640174439706165
nomic-embed-text, 2, 0.031086826881288943, 0.0, 0.9875264930724384, 0.9921674207710467
qwen3-embedding, 1, 0.1782473672307131, 0.19999999999999996, 0.8863086566279608, 0.8518453918955137
qwen3-embedding, 2, 0.08239938172103356, 0.0, 0.9667664045397575, 0.9789668754552034
...
```

##### Column Description
`model` (str) - name of the embedding model, used to obtain embeddings for the similarity measures
`ent_group` (int) {1,2} - id of list of generated entities, for which similarity metric were calculated with comparison to ground truth entities
`cde` (float64) - results of the CDE measure
`ef` (float64) - results of the EF measure
`cdef_05` (float64) - results of the CDEF metric with beta=0.5
`cdef_1` (float64) - results of the CDEF metric with beta=1.0