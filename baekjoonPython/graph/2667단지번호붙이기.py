import sys
from collections import deque

input = sys.stdin.readline


n = int(input())

l = [list(map(str,input().strip())) for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,-1,0,1]
isUsed =[[False]*n for _ in range(n) ]

ans =[]

def BFS(start):
    isUsed[start[0]][start[1]] = True
    cnt = 1
    q = deque()
    q.append(start)
    while q:
        x,y = q.popleft()
        for i in range(4):
            xa = x+dx[i]
            ya = y+dy[i]
            
            if xa<0 or ya<0 or xa>=n or ya>=n: continue
            if isUsed[xa][ya] or l[xa][ya] =='0': continue
            isUsed[xa][ya] = True
            q.append((xa,ya))
            cnt +=1
    ans.append(cnt)
            
for i in range(n):
    for j in range(n):
        if not isUsed[i][j] and l[i][j] =='1':
            BFS((i,j))
ans.sort()
print(len(ans))
for i in ans:
    print(i)