H = [8, 8, 5, 7, 9, 8, 7, 4, 8]

def solution(H):
	stack  = []
	count = 0
	for i in range(0, len(H)):
		while len(stack) != 0  and stack[-1] < H[i]:
			stack.pop()
		if(len(stack)) :
			count += 1
			stack.push(H[i])
		elif(len(stack) != 0 and stack[-1] > H[i]):
			count += 1
			stack.push(H[i])
	return count

print(solution(H))