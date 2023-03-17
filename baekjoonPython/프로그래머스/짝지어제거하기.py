def solution(s):
    answer = 0
    
    q = []
    
    for i in s:
        q.append(i)
        
        while q and len(q)>1:
            if q[-1] == q[-2]:
                q.pop()
                q.pop()
            else:
                break
    
    
    
    
    
    
    return answer


solution('baabaa')