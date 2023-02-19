from collections import deque
def solution(maps):
    answer = []
    
    isVisited =[[0]*len(maps[0]) for _ in range(len(maps))]
    
    # X 바다, 숫자 -> 무인도
    def BFS(a,b,maps):
        q = deque()
        
        isVisited[a][b] = 1
        value = int(maps[a][b])
        q.append([a,b])
        
        dx = [0,1,0,-1]
        dy = [1,0,-1,0]
        X = len(maps)
        Y = len(maps[0])
        while q:
            x,y = q.popleft()
            for i in range(4):
                xa = x + dx[i]
                ya = y + dy[i]
                
                if xa < 0 or ya < 0 or xa >= X or ya >= Y: continue
                
                if maps[xa][ya] == 'X': continue
                
                if not isVisited[xa][ya]:
                    value += int(maps[xa][ya])
                    isVisited[xa][ya] = 1
                    q.append([xa,ya])
        return value
    
    for i in range(len(maps)):
        for j in range(len(list(maps[i]))):
            if maps[i][j] != 'X' and not isVisited[i][j]:
                answer.append(BFS(i,j,maps))
            
    
    if answer:
        return sorted(answer)
    else:
        return [-1]
    
    
    

solution(["X591X","X1X5X","X231X", "1XXX1"])