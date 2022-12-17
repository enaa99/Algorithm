import sys
from collections import deque
input = sys.stdin.readline

# 1 이동가능 // 0 이동불가 


N,M  = map(int,input().split())

l = [[int(i) for i in input().strip()]for i in range(N)]
isUsed =[[False for _ in range(M)]for i in range(N)]

dx = [1,0,-1,0]
dy = [0,-1,0,1]

memo = [[0 for _ in range(M)]for i in range(N)]
q= deque()

q.append((0,0))
while q:
    x,y = q.popleft()
    for i in range(4):
        xa = x +  dx[i]
        ya = y +  dy[i]
        
        if isUsed[xa][ya]:continue
        if xa < 0 or xa >=N or ya<0 or ya >=M:
            continue
        if l[xa][ya] ==0:
            continue
        isUsed[xa][ya] = True
        memo[xa][ya] = memo[x][y] + 1
        q.append((xa,ya))

print(memo[N-1][M-1]+1)

