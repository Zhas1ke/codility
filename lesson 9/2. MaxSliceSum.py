B = [-10,-1,-2,-4,-6]
def solution(A):
    _min = min(max(A), 0)
    max_ending = max_slice = _min
    for a in A:
	    max_ending = max(_min, max_ending + a)
	    max_slice = max(max_slice, max_ending)
    return max_slice
print(solution(B))