import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

dx = [1,0,-1,0]
dy = [0,1,0,-1]


def BFS(a,b):
    q = deque()
    q.append([a,b])
    while q:
        x,y = q.popleft()
        
        for i in range(4):
            xa = x+dx[i]
            ya = y+dy[i]
            
            if xa <0 or ya<0 or xa>=N or ya>=M or isVisited[xa][ya] or graph[xa][ya] == 0: continue
            isVisited[xa][ya] = 1
            q.append([xa,ya])



for _ in range(T):
    M,N,K = map(int,input().split())
    
    graph = [[0]*M for _ in range(N)]
    isVisited =[[0]*M for _ in range(N)]
    for _ in range(K):
        a,b = map(int,input().split())
        graph[b][a] = 1
    
    answer = 0
    for i in range(N):
        for j in range(M):
            if not isVisited[i][j] and graph[i][j] == 1:
                BFS(i,j)
                answer +=1
    
    print(answer)
    