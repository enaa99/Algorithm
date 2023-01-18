def solution(x,n):
    answer = []
    k = x
    while len(answer) < n:
        answer.append(k)
        k += x
    
    
    
    return answer