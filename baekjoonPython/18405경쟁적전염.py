import sys
from collections import deque
input = sys.stdin.readline

N,K = map(int,input().split())

dx = [1,0,-1,0]
dy = [0,-1,0,1]

l= [list(map(int,input().split())) for _ in range(N)]


# S 몇초 후/ X,Y 행열

S,X,Y = map(int,input().split())


start = []

for i in range(N):
    for j in range(N):
        if l[i][j] != 0:
            start.append((l[i][j],i,j))
            # heapq.heappush(start,(l[i][j],i,j))
start.sort()
q= deque()
def BFS():
    length = len(start)
    for _ in range(length):
        v = start.pop(0)
        q.append(v)
        isUsed[v[1]][v[2]] = True
        while q:
            z,x,y = q.popleft()
            
            for i in range(4):
                xa = x + dx[i]
                ya = y + dy[i]
            
                if xa<0 or ya<0 or xa>=N or ya>=N:continue
                if isUsed[xa][ya]:continue
                isUsed[xa][ya] = True
                if l[xa][ya] == 0:
                    l[xa][ya] = z
                    start.append((z,xa,ya))

for _ in range(S):
    isUsed =[[False for _ in range(N)]for i in range(N)]
    BFS()
print(l[X-1][Y-1])