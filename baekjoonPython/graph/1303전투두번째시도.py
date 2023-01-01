import sys
from collections import deque

input = sys.stdin.readline

N,M = map(int,input().split())

graph = [list(map(str,input().rstrip())) for _ in range(M)]

isUsed = [[0]*N for _ in range(M)]


dx = [0,1,0,-1]
dy = [1,0,-1,0]

def BFS(a,b):
    isUsed[a][b] = 1
    cnt = 1
    q = deque()
    q.append((a,b))
    
    color = graph[a][b]
    while q:
        x,y = q.popleft()
        
        for i in range(4):
            xa = x+dx[i]
            ya = y+dy[i]
            
            if xa <0 or ya<0 or xa>=M or ya>=N or isUsed[xa][ya]: continue
            
            if graph[xa][ya] == color:
                isUsed[xa][ya] = 1
                q.append((xa,ya))
                cnt += 1
    return cnt*cnt

white = black = 0
for i in range(M):
    for j in range(N):
        if not isUsed[i][j]:
            if graph[i][j] == 'W':
                white += BFS(i,j)
            else:
                black += BFS(i,j)

print(white ,black)