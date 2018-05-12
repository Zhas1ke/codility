def create_peaks(A):
    N = len(A)
    peaks = [0] * N
    for i in range(1, N - 1):
        if A[i] > max(A[i - 1], A[i + 1]):
            peaks[i] = 1
    return peaks

import math
def divisors(N):
	_list = list()
	for i in range(1, int(math.sqrt(N)) + 1):
		if N % i == 0:
			_list.append(i)
			_list.append(N // i)
	_list.append(N)
	_list = list(set(_list))
	_list.sort()
	return _list

def blocks(A, K):
	return [(i*K, i*K + K) for i in range(len(A)//K)]

def solution(A):
	N = len(A)
	_divisors = divisors(N)
	peaks = create_peaks(A)

	if sum(peaks) <= 1:
		return sum(peaks)

	if len(_divisors) <= 2:
		return 1

	for K in _divisors:
		_blocks_indices = blocks(A, K)
		for (start, end) in _blocks_indices:
			f = True
			_num_peaks = sum(peaks[start:end])
			if _num_peaks < 1:
				f = False
				break
		if f:
			return N // K
	return 0

print(solution([1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]))