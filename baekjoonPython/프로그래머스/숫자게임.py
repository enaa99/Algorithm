def solution(A, B):
    answer = 0
    
    
    A.sort()
    B.sort()
    
    idx = 0
    
    for i in A:
        while idx < len(B):
            if B[idx] > i:
                answer +=1
                idx +=1
                break
            idx+=1
    
    
    
    return answer