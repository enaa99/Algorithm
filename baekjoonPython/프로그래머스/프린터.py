
from collections import deque
def solution(priorities,location):
    answer = 0 
    
    q = deque()
    
    for i in range(len(priorities)):
        q.append([priorities[i],i])
    
    
    while q:
        v,i = q.popleft()
        
        if q:
            k = max(q)
            if v < k[0]:
                q.append([v,i])
                continue
        answer += 1
        if i == location:
            return answer
    
solution([2,1,3,2],2)