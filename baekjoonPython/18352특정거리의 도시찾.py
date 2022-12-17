import sys
from collections import deque

input = sys.stdin.readline


# 도시의 개수 :N / 도로의 개수: M / 거리 정보: K / 출발 도시의 번호 : X
N, M, K, X = map(int,input().split())

l = [[]for _ in range(N+1)]
memo = [0]*(N+1)

for _ in range(M):
    a,b = map(int,input().split())
    l[a].append(b)



q = deque()
isUsed=[False]*(N+1)
def BFS(cnt):
    q.append(cnt)
    isUsed[cnt] = True
    
    while q:
        v = q.popleft()
        for i in l[v]:
            if not isUsed[i]:
                isUsed[i] = True
                q.append(i)
                memo[i] = memo[v] + 1

BFS(X)
if K not in memo:
    print(-1)

else:
    for i in range(1,len(memo)):
        if memo[i] == K:
            print(i)