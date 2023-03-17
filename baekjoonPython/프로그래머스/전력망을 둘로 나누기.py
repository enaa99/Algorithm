import sys
from collections import deque
def solution(n,wires):
    answer = sys.maxsize
    
    
    graph = [[]for _ in range(n+1)]
    
    for a,b in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    
    for x,y in wires:
        graph[x].remove(y)
        graph[y].remove(x)
        
        
        isVisted = [0]*(n+1)
        q = deque()
        q.append(x)
        cnt = 0
        isVisted[x] = 1
        while q:
            v = q.popleft()
            cnt +=1
            
            for i in graph[v]:
                if not isVisted[i]:
                    isVisted[i] = 1
                    q.append(i)
        
        graph[x].append(y)
        graph[y].append(x)
        
        answer = min(answer,abs(n-cnt*2))
        
    
    
    
    
    return answer