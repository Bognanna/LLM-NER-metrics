def precision(tp, fp, fn):
    return tp/(tp+fp)

def recall(tp, fp, fn):
    return tp/(tp+fn)

def f1_score(tp, fp, fn):
    prec = tp/(tp+fp)
    rec = tp/(tp+fn)
    f1 = 0 if (not prec) and (not rec) else 2*(prec*rec)/(prec+rec)
    return f1