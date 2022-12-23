import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

# 9 아기상어의 위치 / 크기 :2 
# 자기자신보다 작은 물고기만 먹을 수 있다

graph = [list(map(int,input().split())) for _ in range(N)]

fish = False
for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            m,n = i,j
            graph[i][j] = 0
            fish = True
            break
    if fish: break


dx = [0,-1,1,0]
dy = [1,0,0,-1]

def BFS(x,y,size):
    fishes = deque()
    distance =[[0]*N for _ in range(N)]
    isUsed =[[False]*N for _ in range(N)]
    l = []

    isUsed[x][y] = True
    fishes.append((x,y))
    
    while fishes:
        a,b= fishes.popleft()
        
        for i in range(4):
            xa = a + dx[i]
            ya = b + dy[i]
            
            if xa < 0 or ya < 0 or xa >= N or ya >= N or isUsed[xa][ya]: continue
            if graph[xa][ya] > size: continue
            
            isUsed[xa][ya] = True
            distance[xa][ya] += distance[a][b]+1
            fishes.append((xa,ya))
            
            if graph[xa][ya] < size and graph[xa][ya] != 0:
                l.append((xa,ya,distance[xa][ya]))
    return l

height = 2
time = 0
cnt =0
while True:
    food:list = BFS(m,n,height)
    
    if not food: break
    
    food.sort(key=lambda x:(x[2],x[0],x[1]))
    m, n, h = food.pop(0)
    graph[m][n] =0
    
    time += h
    cnt += 1
    if cnt == height:
        height +=1
        cnt = 0
print(time)
