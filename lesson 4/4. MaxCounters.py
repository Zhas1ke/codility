A = [3,4,4,6,1,4,4]
N = 5

def solution(N, A):    
    counter = [0] * (N)
    new_max = 0
    old_max = 0
    
    for i in A:
        if i != N + 1:
            if counter[i - 1] > old_max:
                counter[i - 1] += 1
            else:
               counter[i - 1] = old_max + 1 
            
            if counter[i - 1] > new_max:
                new_max += 1
        else:
            old_max = new_max

    for i in range(0, N):
        counter[i] = max(counter[i], old_max)  

    return counter

solution(N, A)