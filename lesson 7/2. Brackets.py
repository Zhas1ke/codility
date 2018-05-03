S = '{[()()]}'
def pair(bracket):
	if bracket == '(':
		return ')'
	if bracket == '{':
		return '}'
	if bracket == '[':
		return ']'

def solution(S):
	stack = list()
	for i in range(0, len(S)):
		if S[i] in ['(','[','{']:
			stack.append(S[i])
		elif len(stack) > 0 and S[i] == pair(stack[-1]):
			del stack[-1]
		else:
			return 0
	if len(stack) == 0:
		return 1
	else:
		return 0
solution(S)