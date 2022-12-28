import sys
import heapq

input = sys.stdin.readline


dx = [1,0,-1,0]
dy = [0,-1,0,1]

def dijkstra(v):
    q = []
    q.append((v,0,0))
    isUsed[0][0] = True
    while q:
        value,x,y= heapq.heappop(q)
        if x == y == N-1:
            return value
        
        for i in range(4):
            xa = x + dx[i]
            ya = y + dy[i]
            
            if xa < 0 or ya <0 or xa>=N or ya>= N or isUsed[xa][ya]: continue
            
            isUsed[xa][ya] = True
            heapq.heappush(q,(value+graph[xa][ya],xa,ya))
cnt = 1
while True:
    
    N = int(input())
    
    if N == 0: 
        exit(0)
    
    graph = [list(map(int,input().split())) for _ in range(N)]
    isUsed = [[False]*N for _ in range(N)]
    
    ans = dijkstra(graph[0][0])
    print(f"Problem {cnt}: {ans}")
    cnt +=1