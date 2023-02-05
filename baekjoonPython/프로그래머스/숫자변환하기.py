from collections import deque
from collections import defaultdict

def solution(x,y,n):
    
    num = defaultdict(int)
    
    def BFS(x,y,n):
        q = deque()
        
        q.append([0,x])
        while q:
            cnt,v= q.popleft()
            
            if v == y:
                return cnt

            for i in ([v+n,v*2,v*3]):
                if num: continue
                if i>y: break
                q.append([cnt+1,i])
            
        return -1
    
    return  BFS(x,y,n)


solution(10,40,5)