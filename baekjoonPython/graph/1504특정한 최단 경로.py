import sys;
input = sys.stdin.readline
from heapq import heappush, heappop

def dijkstra(start, end):
    dis = [sys.maxsize] * (N + 1)
    dis[start] = 0
    q = [[0, start]]
    while q:
        k, u = heappop(q)
        if k > dis[u]: continue
        for w, v in G[u]:
            if dis[v] > dis[u] + w:
                dis[v] = dis[u] + w
                heappush(q, [dis[v], v])

    return dis[end]

N, E = map(int, input().split())
G = [[] for _ in range(N + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    G[u].append([w, v])
    G[v].append([w, u])

stop1, stop2 = map(int, input().split())

# 1 -> stop1 -> stop2 -> N
path1 = dijkstra(1, stop1) + dijkstra(stop1, stop2) + dijkstra(stop2, N)
# 1 -> stop2 -> stop1 -> N
path2 = dijkstra(1, stop2) + dijkstra(stop2, stop1) + dijkstra(stop1, N)

if path1 >= sys.maxsize and path2 >= sys.maxsize:
    print(-1)
else:
    print(min(path1, path2))