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
    if leader == -1:
    	return 0

    cumsum = list()
    leader_positions = list()
    leader_count = 0
    for i in range(len(A)):
    	if A[i] == leader:
    		leader_count +=1
    		leader_positions.append(1)
    	else:
    		leader_positions.append(0)
    	if i == 0:
    		cumsum.append(leader_positions[i])
    	else:
    		cumsum.append(leader_positions[i] + cumsum[i-1])

    EquiLeader_count = 0
    for i in range(1, len(A)):
    	leader_count_left = cumsum[i-1]
    	leader_count_right = leader_count - leader_count_left
    	if leader_count_left > i / 2 and leader_count_right > (len(A)-i)/2:
    		EquiLeader_count += 1
    return EquiLeader_count
A = [4,3,4,4,4,2]
s = solution(A)
print(s)