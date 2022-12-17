import sys
from collections import deque

input = sys.stdin.readline

N,Q = map(int,input().split())

graph = [[]for _ in range(N+1)]
for i in range(N-1):
    p,q,r = map(int,input().split())
    graph[p].append((q,r))
    graph[q].append((p,r))
    
for i in range(Q):
    k,v = map(int,input().split())
    q = deque()
    q.append(v)
    l = []
    isUsed =[False]*(N+1)
    while q:
        port = q.popleft()
        isUsed[port] = True
        l.append(port)
        for connect,val in graph[port]:
            if val >= k and not isUsed[connect]:
                q.append(connect)
    print(len(l)-1)