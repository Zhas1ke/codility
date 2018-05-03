# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def goldenLeader(A):
	n = len(A)
	size = 0
	for k in range(n):
		if (size == 0):
			size += 1
			value = A[k]
		else:
			if (value != A[k]):
				size -= 1
			else:
				size += 1
	candidate = -1
	if (size > 0):
		candidate = value
	leader = -1
	count = 0
	for k in range(n):
		if (A[k] == candidate):
			count += 1
	if (count > n // 2):
		leader = candidate
	return leader

def solution(A):
    # write your code in Python 3.6
    leader = goldenLeader(A)
    for i in range(len(A)):
        if A[i] == leader:
            return i
    return -1