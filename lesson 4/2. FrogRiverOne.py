def solution(X, A):
    s = set(range(1, X + 1))
    for i, x in enumerate(A):
        try:
            s.remove(x)
        except:
            pass
        if len(s) == 0:
            return i
    return -1