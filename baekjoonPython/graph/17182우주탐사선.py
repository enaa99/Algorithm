import sys

input = sys.stdin.readline

# 행성의 개수 N, 발사되는 위치 K
N,K = map(int,input().split())

planets = [list(map(int,input().split()))for _ in range(N)]


for k in range(N):
    for i in range(N):
        for j in range(N):
            planets[i][j] = min(planets[i][j],planets[i][k]+planets[k][j])

isVisited = [0]*N
answer = sys.maxsize

def DFS(cnt,start,v):
    global answer
    
    if cnt == N:
        answer = min(answer,v)
        return
    
    for i in range(len(planets[start])):
        if not isVisited[i]:
            isVisited[i] = True
            DFS(cnt+1,i,v+planets[start][i])
            isVisited[i] = False
            
isVisited[K] =True
DFS(1,K,0)
print(answer)