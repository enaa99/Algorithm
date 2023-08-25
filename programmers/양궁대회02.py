from collections import deque

def solution(n, info):
    
    answer = bfs(n,info)
    
    if not answer:
        return [-1]
    
    
    return answer



def bfs(n,info):
    high_point = 0
    
    res = []
    q = deque()
    q.append([0,[0,0,0,0,0,0,0,0,0,0,0]])
    
    while q:
        focus, point = q.popleft()
        
        if sum(point) == n:
            apeach = rion = 0
            for i in range(11):
                if point[i]== 0 and info[i] == 0:
                    continue
                if point[i] > info[i]:
                    rion += 10 - i
                else:
                    apeach += 10 -i
            
            if rion > apeach and rion >= high_point:
                res = point.copy()
                
                high_point = rion
                
        
        elif sum(point) > n:
            continue
        
        elif focus == 10:
            tmp = point.copy()
            tmp[focus] = n - sum(tmp)
            q.append([-1,tmp])
            
        else:
            q.append([focus+1,point.copy()])
            
            point[focus] = info[focus] +1
            q.append([focus+1,point.copy()])
    return res



solution(5,[2,1,1,1,0,0,0,0,0,0,0])