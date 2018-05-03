A = [1,5,2,1,4,0]

from bisect import bisect_right

def solution(A):
    N = len(A)
    pairs = 0
    
    ranges = sorted( [(i - A[i], i + A[i]) for i in range(N)] )
    starts = [x[0] for x in ranges]
    
    for i in range(N):
        count = bisect_right(starts, ranges[i][1]) - (i + 1)
        pairs += count
        
        if pairs > 10_000_000:
            return -1
            
    return pairs

s = solution(A)
print(s)

A = (1,2,4,7,7,9,9,9)

# def solution(A):
#     pairs = 0
#     ranges = sorted( [(i-A[i], i+A[i]) for i in range(len(A))] )
#     starts = [i[0] for i in ranges]
#     for i in range(len(starts)):
#         count = bisect_right(starts, ranges[i][1])
#         count -= (i+1)
#         pairs += count
#         if pairs > 10_000_000:
#             return -1
#     return pairs