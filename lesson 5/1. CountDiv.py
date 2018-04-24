# A = 11, B = 345, K = 17, ANSWER = 20
# A = B in {0,1}, K = 11, ANSWER = 1
# A = 10, B = 10, K in {5,7,20}, ANSWER = 1


A = -10
B = 1
K = 11
def solution(A, B, K):        
    
    A1 = (A-1) // K
    B1 = B // K
    
    print(A1)
    print(B1)
    return B1 - A1

a = solution(A, B, K)
print(a)