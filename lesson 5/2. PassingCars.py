A =  [0,1,0,1,1]
def solution(A):
	counter = 0
	_sum = 0
	for i in A:
		if i == 0:
			counter += 1
		else:
			_sum += counter
		if _sum > 1_000_000_000:
			return -1
	return _sum