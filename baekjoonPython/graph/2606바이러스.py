import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
graph = [[]for _ in range(N+1)]

isUsed =[0]*(N+1)

for _ in range(int(input())):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)



def BFS():
    cnt = 0
    q = deque()
    q.append(1)
    isUsed[1] = 1
    
    while q:
        v = q.popleft()
        
        for next in graph[v]:
            if not isUsed[next]:
                isUsed[next] = 1
                q.append(next)
                cnt += 1
    return cnt

print(BFS())