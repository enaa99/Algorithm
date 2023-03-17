def solution(s):
    
    
    q = []
    
    for i in s:
        q.append(i)
        
        while q and len(q)>1:
            if q[-1] == q[-2]:
                q.pop()
                q.pop()
            else:
                break
    
    if q:
        return 0
    else:
        return 1
    
    


solution('baabaa')