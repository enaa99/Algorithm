from collections import deque

def solution(wallpaper):
    answer =[]
    
    isVisited =[[0]*len(wallpaper[0]) for _ in range(len(wallpaper))]
    
    X = []
    Y = []
        
    
    def BFS(a,b):
        
        dx = [1,0,-1,0]
        dy = [0,1,0,-1]
        
        N = len(wallpaper)
        M = len(wallpaper[0])
        
        q = deque()
        q.append([a,b])
        while q:
            x,y = q.popleft()
            
            if wallpaper[x][y] == '#':
                X.append(x)
                X.append(x+1)
                Y.append(y)
                Y.append(y+1)
            
            
            for i in range(4):
                xa = x + dx[i]
                ya = y + dy[i]
                
                if xa < 0 or ya < 0 or xa >= N or ya >= M or isVisited[xa][ya]: continue
                
                isVisited[xa][ya] = 1
                q.append([xa,ya])
    
    
    flag = 0
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if not isVisited[i][j] and wallpaper[i][j] == '#':
                BFS(i,j)
                flag = 1
                break
        if flag:
            break
    
    answer.append(min(X))
    answer.append(min(Y))
    answer.append(max(X))
    answer.append(max(Y))
    
    
    return answer

solution([".#...", "..#..", "...#."])