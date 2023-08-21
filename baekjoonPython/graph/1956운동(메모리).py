import sys

input = sys.stdin.readline

INF = sys.maxsize


V,E = map(int,input().split())

dist = [[sys.maxsize] * (V+1) for _ in range(V+1)]

for _ in range(E):
    x, y, c = map(int, input().split())
    dist[x][y] = c

            
            
for k in range(1, V + 1):
    for a in range(1, V + 1):
        for b in range(1, V + 1):
            dist[a][b] = min(dist[a][b], dist[a][k] + dist[k][b])
            
            
answer = sys.maxsize

for i in range(1,V+1):
    answer = min(answer, dist[i][i])
    
if answer != sys.maxsize:
    print(answer)
else:
    print(-1)