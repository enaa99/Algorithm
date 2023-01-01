import sys

input = sys.stdin.readline

N,M = map(int,input().split())

graph = []

isUsed = [[0]*M for _ in range(N)]

x,y,d = map(int,input().split())


dx = [-1,0,1,0]
dy = [0,1,0,-1]

for _ in range(N):
    graph.append(list(map(int,input().split())))

isUsed[x][y] = 1
cnt = 1

while True:
    check = 0
    for _ in range(4):
        d = (d+3)%4
        
        xa = x + dx[d]
        ya = y + dy[d]

        if xa < 0 or ya < 0 or xa>=N or ya>=M or graph[xa][ya] == 1: continue
        
        if not isUsed[xa][ya]:
            isUsed[xa][ya] = 1
            x = xa
            y = ya
            
            cnt += 1
            check = 1
            break
        
    if check == 0:
        if graph[x-dx[d]][y-dy[d]] == 1:
            print(cnt)
            exit(0)
        else:
            x,y = x-dx[d],y-dy[d]