import sys
from collections import deque

input = sys.stdin.readline


N,M = map(int,input().split())

indegree =[0]*(N+1)

graph = [[]for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    indegree[b] += 1
    graph[a].append(b)
    
q = deque()

for i in range(1,N+1):
    if indegree[i] == 0:
        q.append(i)
        
answer =[]
while q:
    
    v = q.popleft()
    answer.append(v)
    
    for i in graph[v]:
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)

print(*answer, sep=" ")