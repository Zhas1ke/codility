def solution(A):
    # write your code in Python 3.6
    minValue = (A[0] + A[1]) / 2
    minIndex = 0
    N = len(A)
    
    for i in range(N - 2):
        val2 = (A[i] + A[i+1]) / 2
        val3 = (A[i] + A[i+1] + A[i+2]) / 3
        if minValue > min(val2, val3):
            minValue = min(val2, val3)
            minIndex = i
    
    lastCheck = (A[N-2] + A[N-1]) / 2
    if lastCheck < minValue:
        minIndex = N - 2
    
    return minIndex