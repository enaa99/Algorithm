import sys
from collections import deque

input = sys.stdin.readline

N,M = map(int,input().split())

l = [[i for i in input().strip()]for _ in range(N)]

dx = [0,1]
dy=  [1,0]

q = deque()
isUsed = [[False for _ in range(M)]for i in range(N)]
x,y = 0, 0

cnt = 0
def BFS1(start):
    isUsed[start[0]][start[1]] = True
    q.append(start)
    while q:
        x,y = q.popleft()
        
        xa = x + dx[0]
        xy = y + dy[0]
        
        if xa >= N or xy >= M: continue
        if isUsed[xa][xy]:continue
        if l[xa][xy] == '-':
            q.append((xa,xy))
            isUsed[xa][xy] = True

q2 = deque()
def BFS2(start):
    isUsed[start[0]][start[1]] = True
    q2.append(start)
    while q2:
        x,y = q2.popleft()
        xa = x+dx[1]
        ya = y+dy[1]
        
        if xa>=N or ya>=M : continue
        if isUsed[xa][ya]: continue
        if l[xa][ya] =='|':
            q2.append((xa,ya))
            isUsed[xa][ya]=True

for i in range(N):
    for j in range(M):
        if l[i][j] =='-' and not isUsed[i][j]:
            BFS1((i,j))
            cnt+=1
        elif l[i][j] =='|' and not isUsed[i][j]:
            BFS2((i,j))
            cnt+=1

print(cnt)