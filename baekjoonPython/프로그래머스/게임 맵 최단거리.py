from collections import deque

def solution(maps):
    answer = 0
    
    # n,m에 위치
    # 0은 벽, 1은 공간
    N = len(maps)
    M = len(maps[0])
    
    isVisited = [[0]*M for _ in range(N)]
    dx = [1,0,-1,0]
    dy = [0,-1,0,1]
    
    def BFS():
        q = deque()
        q.append([N-1,M-1,1])
        
        while q:
            x,y,v = q.popleft()
            
            if x == 0 and y == 0:
                return v
            
            
            for i in range(4):
                xa = x + dx[i]
                ya = y + dy[i]
                
                if xa < 0 or ya < 0 or xa>=N or ya>=M: continue
                
                if isVisited[xa][ya] or maps[xa][ya] == 0: continue
                
                isVisited[xa][ya] = 1
                q.append([xa,ya,v+1])
                
        return -1
        
    return BFS()
    
    