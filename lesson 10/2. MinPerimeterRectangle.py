import math
def solution(N):
	min_p = (N+1)*2
	for x in range(1, int(math.sqrt(N)) + 1):
		if N % x == 0:
			y = int(N / x)
			min_p = min(min_p, 2*(x+y))
	return min_p
print(solution(30))