import sys
from collections import deque

input = sys.stdin.readline

N,M = map(int,input().split())

graph_low = [[]for _ in range(N+1)]
graph_high = [[]for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    graph_low[b].append(a)
    graph_high[a].append(b)

ans = 0
def BFS(k,graph):
    global ans
    q = deque()
    isUsed[k] = 1
    cnt = 0
    q.append(k)
    while q:
        if cnt >= (N+1)//2:
            ans += 1
            break
        
        v = q.popleft()
        for num in graph[v]:
            if not isUsed[num]:
                isUsed[num] = 1
                q.append(num)
                cnt += 1
            

for i in range(1,N+1):
    isUsed = [0]*(N+1)
    BFS(i,graph_low)

for i in range(N,0,-1):
    isUsed = [0]*(N+1)
    BFS(i,graph_high)


print(ans)