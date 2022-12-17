import sys
from collections import deque

input = sys.stdin.readline

N,M = map(int,input().split())


l = [list(map(int,input().split())) for _ in range(N)]
isUsed =[[False]*M for _ in range(N)]

dx = [1,0,-1,0,1,-1,1,-1]
dy = [0,-1,0,1,-1,1,1,-1]

def BFS(a,b,cnt):
    q = deque()
    
    q.append((a,b,cnt))
    while q:
        x,y,v = q.popleft()
        for i in range(8):
            xa = x + dx[i]
            ya = y + dy[i]

            if xa <0 or ya <0 or xa>= N or ya>=M or isUsed[xa][ya]: continue
            if l[xa][ya] != 0:
                return v
            isUsed[xa][ya] = True
            q.append((xa,ya,v+1))

ans = 0
for i in range(N):
    for j in range(M):
        if l[i][j] == 0 and not isUsed[i][j]:
            isUsed[i][j] = True
            ans = max(ans,BFS(i,j,1))

print(ans)