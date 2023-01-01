import sys

input = sys.stdin.readline

N,M = map(int,input().split())


# bellman-ford


dist = [sys.maxsize]*(N+1)

edges = []

for _ in range(M):
    a,b,c = map(int,input().split())
    edges.append((a,b,c))

def bellman_ford():
    dist[1] = 0
    for i in range(M):
        for cur,next,value in edges:
            if dist[cur] != sys.maxsize and dist[next] > dist[cur] + value:
                dist[next] = dist[cur]+value
                if i == M-1:
                    print(-1)
                    exit(0)

bellman_ford()

for i in range(2,N+1):
    if dist[i] == sys.maxsize:
        print(-1)
    else:
        print(dist[i])