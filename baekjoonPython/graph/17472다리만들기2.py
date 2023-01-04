import sys
from collections import deque
import heapq

input = sys.stdin.readline

N,M = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(N)]

isUsed = [[0]*M for _ in range(N)]

dx = [1,0,-1,0]
dy = [0,-1,0,1]


def BFS(a,b):
    isUsed[a][b] = 1
    q = deque()
    q.append((a,b))
    tmp = []
    tmp.append((a,b))
    while q:
        x,y = q.popleft()       
        for i in range(4):
                    
            xa = x + dx[i]
            ya = y + dy[i]
        
            if xa <0 or ya <0 or xa>=N or ya >=M or isUsed[xa][ya] : continue
            
            if graph[xa][ya] == 1:
                isUsed[xa][ya] = 1
                q.append((xa,ya))
                tmp.append((xa,ya))
    return tmp

        
island = []

for i in range(N):
    for j in range(M):
        if not isUsed[i][j] and graph[i][j] == 1:
            tmp = BFS(i,j)
            island.append(tmp)

len_island = len(island)

dp = [[sys.maxsize]*len_island for _ in range(len_island)]

for num_1 in range(len_island):
    for num_2 in range(len_island):
        if num_1 == num_2: continue
        for x,y in island[num_1]:
            for xa,ya in island[num_2]:
                if x == xa  and abs(y-ya) > 2:
                    flag = 0
                    if y > ya:
                        for kk in range(ya+1,y):
                            if graph[x][kk] == 1:
                                flag =1
                                break
                        if not flag:
                            dp[num_1][num_2] = dp[num_1][num_2] = min(dp[num_1][num_2],abs(y-ya)-1)
                    else:
                        for kk in range(y+1,ya):
                            if graph[x][kk] == 1:
                                flag =1
                                break
                        if not flag:
                            dp[num_1][num_2] = dp[num_1][num_2] = min(dp[num_1][num_2],abs(y-ya)-1)
                elif y == ya  and abs(x-xa) > 2:
                    flag = 0
                    if x > xa:
                        for kk in range(xa+1,x):
                            if graph[kk][y] == 1:
                                flag =1
                                break
                        if not flag:
                            dp[num_1][num_2] = dp[num_1][num_2] = min(dp[num_1][num_2],abs(x-xa)-1)
                    else:
                        for kk in range(x+1,xa):
                            if graph[kk][y] == 1:
                                flag =1
                                break
                        if not flag:
                            dp[num_1][num_2] = dp[num_1][num_2] = min(dp[num_1][num_2],abs(x-xa)-1)
                        
                    
for i in range(len_island):
    for j in range(len_island):
        if i == j:
            dp[i][j] = 0
        if dp[i][j] == sys.maxsize:
             dp[i][j] = 0
# 모든 경로?
# 플로이드 워셜
# 크루스칼

for k in range(len_island):
    for i in range(len_island):
        for j in range(len_island):
            if dp[i][k] !=0 and dp[k][j] !=0:
                dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])


ans = 0
# def DFS(cnt,v,depth):
#     global ans
#     if depth == len_island-1:
#         ans = min(ans,v)
#         return 
    
    
#     for i in range(len_island):
#         if dp[cnt][i] !=0 and not isVisited[i]:
#             isVisited[i] = 1
#             DFS(i,v+dp[cnt][i],depth+1)
            
# for i in range(len(dp)):
isVisited = [0]*len_island
isVisited[0] = 1
# DFS(0,0,0)
# DFS(0,0,0)
distance =[]
for i in range(len(dp)):
    for j in range(i,len(dp)):
        if dp[i][j] != 0:
            distance.append((dp[i][j],i,j))

distance.sort()
parent = [i for i in range(len(dp))]

def find(n):
    if n == parent[n]:
        return n
    parent[n] = find(parent[n])
    return parent[n]

def union(a,b):
    ra = find(a)
    rb = find(b)
    if ra > rb:
        parent[ra] = rb
    else:
        parent[rb] = ra

cnt = 0
for a,b,c in distance:
    if find(b) != find(c):
        union(b,c)
        ans += a
        cnt +=1

if cnt == len(dp)-1:
    print(ans)
else:
    print(-1)