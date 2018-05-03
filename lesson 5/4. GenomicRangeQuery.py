def solution(S, P, Q):
    # write your code in Python 3.6
	res = []
    
    for x, y in zip(P,Q):
        if 'A' in S[x:y+1]:
            res.append(1)
        elif 'C' in S[x:y+1]:
            res.append(2)
        elif 'G' in S[x:y+1]:
            res.append(3)
        elif 'T' in S[x:y+1]:
            res.append(4)
    
    return res