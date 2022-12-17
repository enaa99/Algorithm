import sys
from collections import deque
input = sys.stdin.readline


N,M = map(int,input().split())

inDegree =[0]*(N+1)
answer = deque()

l = [[]for _ in range(N+1)]

topo = deque()
def topologySort():
    for i in range(1,N+1):
        if inDegree[i] == 0: topo.append(i)
    
    for _ in range(1,N+1):
        if not topo: break
        else:
            v = topo.popleft()
            answer.append(v)
            for i in l[v]:
                inDegree[i] -= 1
                if inDegree[i] == 0: topo.append(i)


for _ in range(M):
    a,b = map(int,input().split())
    l[a].append(b)
    inDegree[b] +=1

topologySort()
print(*answer)