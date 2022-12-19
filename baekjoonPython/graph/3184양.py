import sys
from collections import deque

input = sys.stdin.readline

### . 필드 / # 울타리 / o 양 / v 늑대

R,C = map(int,input().split())


graph = []

lamb = 0
wolf =0

for i in range(R):
    l = list(map(str,input().strip()))
    graph.append(l)

dx = [1,0,-1,0]
dy = [0,-1,0,1]

isUsed =[[False]*C for _ in range(R)]



def BFS(a,b):
    global lamb
    global wolf
    q = deque()
    q.append((a,b))
    isUsed[a][b] = True
    tmp1 = 0
    tmp2 = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            xa = x + dx[i]
            ya = y + dy[i]
            
            if xa < 0 or ya <0 or xa>=R or ya>=C or isUsed[xa][ya] or graph[xa][ya] =='#': continue
            isUsed[xa][ya] = True
            # 늑대를 기준으로 양 늑대 체크
            if graph[xa][ya] == 'o':
                tmp1 += 1
            elif graph[xa][ya] == 'v':
                tmp2 += 1
            q.append((xa,ya))
    if tmp1 <= tmp2:
        wolf += tmp2
        lamb -= tmp1

for i in range(R):
    for j in range(C):
        if not isUsed[i][j] and graph[i][j] == 'v':
            BFS(i,j)
        if graph[i][j] == 'o':
            lamb += 1



print(lamb,wolf, end=" ")