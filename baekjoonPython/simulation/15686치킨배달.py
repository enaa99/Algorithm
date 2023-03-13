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


for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            home.append([i+1,j+1])
        elif graph[i][j] == 2:
            chicken.append([i+1,j+1])



isVisited =[0]*len(chicken)
arr = [0]*M
answer = sys.maxsize


def DFS(cnt,idx):
    global answer
    if cnt == M:
        dist = [sys.maxsize]*len(home)
        for k in range(len(home)):
            for req in arr:
                dist[k] = min(dist[k],abs(req[0]-home[k][0])+abs(req[1]-home[k][1]))
        answer = min(sum(dist),answer)
        
        return
    
    for num in range(idx,len(chicken)):
        if not isVisited[num]:
            arr[cnt] = chicken[num]
            isVisited[num] = 1
            DFS(cnt+1,num+1)
            isVisited[num] = 0
            
DFS(0,0)


print(answer)