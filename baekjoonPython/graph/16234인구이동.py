import sys
from collections import deque

input = sys.stdin.readline

N,L,R = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(N)]


dx = [1,0,-1,0]
dy = [0,-1,0,1]

def BFS(a,b):    
    country = deque()
    q = deque()
    isUsed[a][b] = 1
    q.append((a,b))
    
    while q:
        x,y = q.popleft()
        
        for i in range(4):
            xa = x + dx[i]
            ya = y + dy[i]
            
            if xa < 0 or ya < 0 or xa>=N or ya>=N or isUsed[xa][ya]: continue
            if L <= abs(graph[xa][ya] - graph[x][y]) <= R:
                isUsed[xa][ya] = 1
                q.append((xa,ya))
                country.append((xa,ya))
    return country


def check():
    flag = False
    for i in range(N):
        for j in range(N):
            if not isUsed[i][j]:
                cities = BFS(i,j)
                if cities:
                    sum = 0
                    cities.append((i,j))
                    for x,y in cities:
                        sum += graph[x][y]
                    
                    
                    for x,y in cities:
                        graph[x][y] = sum//(len(cities))
                    flag = True
    return flag            


day =0 

while True:
    isUsed = [[0]*N for _ in range(N)]
    
    if check():
        day +=1
    else:
        print(day)
        break