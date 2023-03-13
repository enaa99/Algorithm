import sys
from collections import deque

input = sys.stdin.readline

# 0 빈칸, 1 집, 2 치킨집

# 하나씩? 치킨 거리를 각각 구한다음 값 설정, 전부다 구한다음 큰거 M개 만큼 뺴기


N, M = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(N)]

home = []
chicken = []

# M 폐업 시키지 않을 개수 
def BFS(a,b):
    q = deque()
    q.append([a,b])
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    
    isVisited = [[0]*N for _ in range(N)]
    
    while q:
        x,y = q.popleft()
        
        if graph[x][y] == 1:
            home.append([xa+1,ya+1])
        elif graph[x][y] == 2 :
            chicken.append([xa+1,ya+1])
        
        for i in range(4):
            xa = x + dx[i]
            ya = y + dy[i]
            if xa < 0 or ya < 0 or ya>=N or xa >= N or isVisited[xa][ya]: continue
            isVisited[xa][ya] = 1
            
            q.append([xa,ya])


BFS(0,0)

dist = []

for x,y in chicken:
    k = sys.maxsize
    for a,b in home:
        k = min(k,abs(x-a)+abs(b-y))
    dist.append(k)

dist.sort()


print(sum(dist[abs(len(dist)-M):]))