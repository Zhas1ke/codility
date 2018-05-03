def MaxSliceSum(A):
    _min = min(max(A), 0)
    max_ending = max_slice = _min
    for a in A:
	    max_ending = max(_min, max_ending + a)
	    max_slice = max(max_slice, max_ending)
    return max_slice

def solution(A):
	if len(A) == 0:
		return 0

	tmp = list()
	for i in range(len(A)):
		if i == 0:
			tmp.append(A[i])
		else:
			tmp.append(A[i] - A[i-1])
	return max(MaxSliceSum(tmp[1:]), 0)

A = [23171, 21011, 21123, 21366, 21013, 21367]
solution(A)