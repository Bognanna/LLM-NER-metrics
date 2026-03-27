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