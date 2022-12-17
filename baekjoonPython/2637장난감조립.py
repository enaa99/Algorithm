import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
M = int(input())

l =[[]for _ in range(N+1)]
count =[[0]*(N+1) for _ in range(N+1)]
inDegree =[0]*(N+1)

# X 만드는데 중간 or 기본 Y가 K개 필요하다
for _ in range(M):
    x,y,k = map(int,input().split())
    l[y].append((x,k))
    inDegree[x] += 1

q = deque()
def topologySort():
    for _ in range(1,N+1):
        if inDegree[_] == 0:
            q.append(_)
    
    while q:
        now = q.popleft()
        for next,next_need in l[now]:
            if count[now].count(0) == N+1:
                count[next][now] += next_need
            else:
                for i in range(1,N+1):
                    count[next][i] += count[now][i] * next_need
            inDegree[next] -= 1
            if inDegree[next] == 0:
                q.append(next)

topologySort()
for x in enumerate(count[N]):
    if x[1]>0:
        print(*x)

