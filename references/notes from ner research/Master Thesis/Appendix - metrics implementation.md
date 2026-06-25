```
def precision(tp: int, fp: int, fn: int) -> float:

    p = tp/(tp+fp) if tp+fp != 0 else 0

    return p

  

def recall(tp: int, fp: int, fn: int) -> float:

    r = tp/(tp+fn) if tp+fn != 0 else 0

    return r

  

def f1_score(tp: int, fp: int, fn: int) -> float:

    p = precision(tp, fp, fn)

    r = recall(tp, fp, fn)

    f1 = 2*(p*r)/(p+r) if p+r != 0 else 0

    return f1
```

```
def soft_matching(

        annotated_spans: list,

        predicted_span: list,

        sim_threshold: float = 0.5

):

    similarity = []

    for t in annotated_spans:

        if predicted_span[1] == t[1]:

            score = SequenceMatcher(None, t[0], predicted_span[0]).ratio()

        else:

            score = 0

        similarity.append(score)  

    score = max(similarity)

    max_index = similarity.index(max(similarity))

    t = annotated_spans[max_index]

    if predicted_span[0] in t[0] or t[0] in predicted_span[0]:

        if score > sim_threshold:

            return True

    return False
```

```
def CDE(gold_embeddings:list, generated_embeddings:list) -> float:

  

    min_len = min(len(gold_embeddings), len(generated_embeddings))

  

    distance_matrix = np.array(

        [[ __cosine_distance_of_embeddings(i,j) for i in gold_embeddings] for j in generated_embeddings]

        )

  

    cumulative_distance = 0.0

  

    while distance_matrix.any():

        max_i, max_j = __find_min_dist(distance_matrix)

        cumulative_distance += distance_matrix[max_i, max_j]

        distance_matrix = np.delete(distance_matrix, max_i, axis=0)

        distance_matrix = np.delete(distance_matrix, max_j, axis=1)

  

    return cumulative_distance/min_len

  

def exhaustive_CDE(gold_embeddings:list, generated_embeddings:list) -> float:

  

    if len(gold_embeddings) < len(generated_embeddings):

        min_len = len(gold_embeddings)

        short_list = gold_embeddings

        long_list = generated_embeddings

    else:

        min_len = len(generated_embeddings)

        short_list = generated_embeddings

        long_list = gold_embeddings

  

    minimal_average_distance = 2.0

  

    for combination in list(combinations(long_list, min_len)):

        for permutation in list(permutations(combination)):

            cumulative_distance = 0.0

  

            for a, b in zip(permutation, short_list):

                cumulative_distance += __cosine_distance_of_embeddings(a, b)

  

            minimal_average_distance = min(

                minimal_average_distance, cumulative_distance/min_len)

    return minimal_average_distance

  

def EF(gold_embeddings:list, generated_embeddings:list) -> float:

    a = len(gold_embeddings)

    b = len(generated_embeddings)

    return 2*b/(a+b) - 1

  

def CDEF(gold_embeddings:list, generated_embeddings:list, beta:float=1) -> float:

    a = 1-CDE(gold_embeddings, generated_embeddings)/2

    b = 1-abs(EF(gold_embeddings, generated_embeddings))

    return (1+beta*beta)*a*b/(beta*beta*a + b)
```