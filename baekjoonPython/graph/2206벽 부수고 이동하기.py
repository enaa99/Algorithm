import sys
import heapq

input = sys.stdin.readline

N,M = map(int,input().split())

graph = [list(map(str,input().rstrip())) for _ in range(N)]

dx = [1,0,-1,0]
dy = [0,-1,0,1]

isUsed = [[[0]*2 for _ in range(M)]for i in range(N)]

def BFS():
    q = []
    q.append((1,0,0,0))
    isUsed[0][0][0] = 1
    
    while q:
        
        cnt,x,y,brk = heapq.heappop(q)
    
        if x == N-1 and y == M-1:
            print(cnt)
            exit(0)
        
        for i in range(4):
            xa = x + dx[i]
            ya = y + dy[i]
            
            if xa < 0 or ya <0 or xa>=N or ya>=M or isUsed[xa][ya][brk] : continue
            
            if graph[xa][ya] == '1':
                if brk >= 1:
                    continue
                else:
                    isUsed[xa][ya][brk] =1
                    heapq.heappush(q,(cnt+1,xa,ya,brk+1))
            else:
                isUsed[xa][ya][brk] = 1
                heapq.heappush(q,(cnt+1,xa,ya,brk))
            
    return -1

print(BFS())