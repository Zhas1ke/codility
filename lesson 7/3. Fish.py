A = [4,3,2,1,5]
B = [0,1,0,0,0]

class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

def solution(A, B):
	N = len(A)
	stack_A = Stack()
	stack_B = Stack()
	for i in range(N - 1, -1, -1):
		if B[i] == 0:
			stack_A.push(A[i])
			stack_B.push(B[i])
		if stack_B.size() == 0:
			stack_A.push(A[i])
			stack_B.push(B[i])
		else:
			while stack_B.peek() != 1 or stack_B.size() > 0:
				if A[i] > stack_A.peek():
					stack_A.pop()
					stack_B.pop()
				else:
					break
	return stack_A.size()
			
s = solution(A, B)
print(s)