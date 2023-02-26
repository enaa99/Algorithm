from collections import deque


def solution(maps):
    answer = 0
    
    N = len(maps)
    M = len(maps[0])
    
    def BFS(a,b,point):
        q = deque()
        q.append([a,b,0])
        
        dx = [1,0,-1,0]
        dy = [0,1,0,-1]
        
        isVisited =[[0]*M for _ in range(N)]
        isVisited[a][b] = 1
        
        while q:
            x,y,v = q.popleft()
            
            if maps[x][y] == point:
                return v
            
            for i in range(4):
                xa = x + dx[i]
                ya = y + dy[i]
                
                if xa <0 or ya <0 or xa>=N or ya>=M: continue
                
                if maps[xa][ya] == 'X' or isVisited[xa][ya]: continue
                
                isVisited[xa][ya] = 1
                q.append([xa,ya,v+1])
        return -1
    
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] == 'S':
                tmp = BFS(i,j,'L')
                if tmp == -1:
                    return -1
                else:
                    answer += tmp
            elif maps[i][j] == 'L':
                k = BFS(i,j,'E')
                if k == -1:
                    return -1
                else:
                    answer += k
    
    
    return answer

solution(["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"])