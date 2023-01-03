import sys
import heapq

input = sys.stdin.readline

N,M,K = map(int,input().split())

# K 1초에 이동할 수 있는 칸의 개수
# 벽 #


gym = [list(map(str,input().rstrip())) for _ in range(N)]

x1,y1,x2,y2 = map(int,input().split())


dx = [1,0,-1,0]
dy = [0,-1,0,1]

isUsed = [[[0]*2 for _ in range(M)]for i in range(N)]

def BFS(a,b):
    q = []
    q.append((0,a,b,-1,0))
    isUsed[a][b][0] = 1
    
    while q:
        cnt,x,y,dir,tmp = heapq.heappop(q)
        
        if x == x2-1 and y == y2-1:
            return cnt
        
        for i in range(4):
            xa = x + dx[i]
            ya = y + dy[i]
            
            if xa < 0 or ya < 0 or xa >= N or ya >= M : continue
            if gym[xa][ya] == '#' : continue
            if isUsed[xa][ya][0] == 1 and isUsed[xa][ya][1] < cnt : continue
            
            isUsed[xa][ya][0] = 1
            isUsed[xa][ya][0] = cnt
            
            if dir == i:
                if tmp >= K:
                    heapq.heappush(q,(cnt+1,xa,ya,dir,1))
                else:
                    heapq.heappush(q,(cnt,xa,ya,dir,tmp+1))
            else:
                    heapq.heappush(q,(cnt+1,xa,ya,i,1))
                
    return -1


print(BFS(x1-1,y1-1))