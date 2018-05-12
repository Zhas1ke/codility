def arrayF(n):
	F = [0] * (n + 1)
	i=2
	while (i * i <= n):
		if (F[i] == 0):
			k=i * i
			while (k <= n):
				if (F[k] == 0):
					F[k] = i;
				k += i
		i += 1
	return F

def factorization(x, F):
	primeFactors = []
	while (F[x] > 0):
		primeFactors += [F[x]]
		x = x // F[x]
	primeFactors += [x]
	return primeFactors

def solution(N, P=None, Q=None):
	F = arrayF(N)
	SemiPrimes = [0]*(N+1)
	for x in range(0, N+1):
		fact = factorization(x, F)
		if len(fact) == 2:
			SemiPrimes[x] = 1
	
	prefix_sum = [0]*(N+1)
	prefix_sum[0] = SemiPrimes[0]
	for i in range(1, N+1):
		prefix_sum[i] = prefix_sum[i-1] + SemiPrimes[i]

	result=list()
	for p, q in zip(P, Q):
		result.append(prefix_sum[q] - prefix_sum[p-1])
	return result