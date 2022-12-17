import sys
from collections import deque

input = sys.stdin.readline

N,M = map(int,input().split())

# B 파란 , W 흰색
isUsed = [[False for _ in range(N)]for i in range(M)]

l = [list(map(str,input().strip())) for _ in range(M)]

dx = [1,0,-1,0]
dy = [0,-1,0,1]

def BFS(o,p):
    cnt = 1
    q = deque()
    q.append((o,p))
    isUsed[o][p] = True
    team = l[o][p]
    while q:
        x,y = q.popleft()
        for i in range(4):
            xa = x +dx[i]
            ya = y +dy[i]
            
            if xa<0 or ya<0 or xa>=M or ya>=N: continue
            
            if l[xa][ya] == team and not isUsed[xa][ya]:
                isUsed[xa][ya] = True
                q.append((xa,ya))
                cnt += 1
    return cnt

b = w = 0
for i in range(M):
    for j in range(N):
        if not isUsed[i][j]:
            k = BFS(i,j)
            if l[i][j] == 'B':
                b += k**2
            else:
                w += k**2

print(w,b, end=' ')