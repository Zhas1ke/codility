import math
def solution(A):
	_set = set()
	for i in range(2, int(math.sqrt(A)) + 1):
		if A % i == 0:
			_set.add(i)
			_set.add(int(A / i))
	_set.add(1)
	_set.add(A)
	return len(_set)

A = 16
print(solution(A))