import numpy as np
from itertools import combinations, permutations

def __cosine_similarity(v1:list, v2:list) -> float:
    v1 = np.squeeze(np.asarray(v1))
    v2 = np.squeeze(np.asarray(v2))
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

def __cosine_distance(v1:list, v2:list) -> float:
    return 1-__cosine_similarity(v1, v2)

def __cosine_distance_of_embeddings(a:list, b:list) -> float:
    
    if a[1] != b[1]: return 2.0

    return __cosine_distance(a[0], b[0])

def __find_min_idx(x):
    k = x.argmin()
    ncol = x.shape[1]
    return int(k/ncol), int(k%ncol)

def CDE(gold_embeddings:list, generated_embeddings:list) -> float:

    min_len = min(len(gold_embeddings), len(generated_embeddings))

    distance_matrix = np.array(
        [[ __cosine_distance_of_embeddings(i,j) for i in gold_embeddings] for j in generated_embeddings]
        )

    cumulative_distance = 0.0

    while distance_matrix.any():
        max_i, max_j = __find_min_idx(distance_matrix)
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

    minimal_cumulative_distance = 2.0

    for combination in list(combinations(long_list, min_len)):
        for permutation in list(permutations(combination)):
            cumulative_distance = 0.0

            for a, b in zip(permutation, short_list):
                cumulative_distance += __cosine_distance_of_embeddings(a, b)

            minimal_cumulative_distance = min(
                minimal_cumulative_distance, cumulative_distance)
    
    return minimal_cumulative_distance/min_len

def EF(gold_embeddings:list, generated_embeddings:list) -> float:
    a = len(gold_embeddings)
    b = len(generated_embeddings)
    return 2*b/(a+b) - 1

def CDEF(gold_embeddings:list, generated_embeddings:list, beta:float=1) -> float:
    a = 1-CDE(gold_embeddings, generated_embeddings)/2
    b = 1-abs(EF(gold_embeddings, generated_embeddings))
    return (1+beta*beta)*a*b/(beta*beta*a + b)


