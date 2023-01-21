import sys
import heapq

input = sys.stdin.readline

M,N = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(N)]

tomato = []
flag = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            tomato.append([0,i,j])


def BFS():
    
    dx =[1,0,-1,0]
    dy = [0,1,0,-1]
    tmp = 0
    while tomato:
        day,x,y, = heapq.heappop(tomato)
        
        for i in range(4):
            xa = x + dx[i]
            ya = y + dy[i]
            
            if xa <0 or ya<0 or xa>=N or ya >=M: continue
            if graph[xa][ya] == 1 or graph[xa][ya] == -1: continue
            
            graph[xa][ya] = 1
            tmp = day+1
            heapq.heappush(tomato,[day+1,xa,ya])
    return tmp

tmp = BFS()

for i in range(N):
    if 0 in graph[i]:
        print(-1)
        exit(0)
print(tmp)
