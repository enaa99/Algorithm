import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

graph = [list(map(str,input().rstrip())) for _ in range(N)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

isVisted = [[0] * N for _ in range(N)]
def BFS(a,b):
    q = deque()
    q.append([a,b])
    start = graph[a][b]
    isVisted[a][b] = 1
    
    check = 0
    
    while q:
        x,y = q.popleft()
        for i in range(4):
            xa = x + dx[i]
            ya = y + dy[i]
            
            if xa<0 or ya<0 or xa>= N or ya>=N or isVisted[xa][ya]: continue
            
            
            
            if graph[xa][ya] == start:
                isVisted[xa][ya] = 1
                q.append([xa,ya])
    return check
tmp = 0
green = 0
for i in range(N):
    for j in range(N):
        if not isVisted[i][j]:
            green += BFS(i,j)
            tmp +=1 

for i in range(N):
    for j in range(N):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

isVisted = [[0]*N for _ in range(N)]
tmp2 = 0
for i in range(N):
    for j in range(N):
        if not isVisted[i][j]:
            BFS(i,j)
            tmp2 +=1 
            

print(tmp,tmp2)