def create_peaks(A):
    N = len(A)
    peaks = [False] * N
    for i in range(1, N - 1):
        if A[i] > max(A[i - 1], A[i + 1]):
            peaks[i] = True
    return peaks

def check(x, A):
    flags = x
    pos = 0
    while pos < N and flags > 0:
        if peaks[pos]:
            flags -= 1
            pos += x
        else:
            pos += 1
    return flags == 0

def solution(A):
    global peaks, N
    peaks = create_peaks(A)
    N = len(A)
    l = 1
    r = len(peaks)
    i = mid = len(peaks) // 2
    while l < r:
        mid = ( l + r ) // 2
        if check(mid, A):
            l = mid + 1
        else:
            r = mid
    return l-1

A = [1,5,3,4,3,4,1,2,3,4,6,2]
print(solution(A))
print(diff(solution(A)))