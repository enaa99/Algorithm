import sys
from collections import deque

input = sys.stdin.readline

## F 불, # 벽, J 미로에서 초기 위치, . 지나갈 수 있는 공간

R,C = map(int,input().split())

graph = [list(map(str,input().rstrip())) for _ in range(R)]

fire = deque()
for i in range(R):
    for j in range(C):
        if graph[i][j] == 'J':
            a,b = i,j
        elif graph[i][j] == 'F':
            fire.append([i,j,0])


def find_way():
    q = deque()
    cnt = 0
    
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    
    q.append([a,b,0])
    
    while q:
        while fire and cnt >= fire[0][2]:
            x,y,tmp = fire.popleft()
            
            for i in range(4):
                xa = x + dx[i]
                ya = y + dy[i]
                
                if xa < 0 or ya < 0 or xa >=R or ya >=C: continue
                
                if graph[xa][ya] == '.' or graph[xa][ya] == 'J':
                    graph[xa][ya] = 'F'
                    fire.append([xa,ya,tmp+1])
                    
        while q and cnt >= q[0][2]:
            x,y,v = q.popleft()
            
            for i in range(4):
                xa = x + dx[i]
                ya = y + dy[i]
                
                
                if xa < 0 or ya < 0 or xa >=R or ya >=C: 
                    return v + 1
                
                elif graph[xa][ya] == '.':
                    graph[xa][ya] = 'J'
                    q.append([xa,ya,v+1])
        cnt += 1
    return 'IMPOSSIBLE'

print(find_way())