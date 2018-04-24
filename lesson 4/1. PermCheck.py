def solution(A):
    s = set(list(range(1, len(A) + 1)))
    for x in A:
        try:
            s.remove(x)
        except:
            return 0
    return 1