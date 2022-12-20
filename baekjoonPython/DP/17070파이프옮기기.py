import sys
from collections import deque


input = sys.stdin.readline

dx =[1,1,0]
dy =[0,1,1]

N = int(input())

# 대각선으로 왔을 때만
# 아래로 갈땐 우측 못감 대각선만 갈 수 있다.

graph = [list(map(int,input().split())) for _ in range(N)]
dp = [[-1]*N for _ in range(N)]

def DFS(a1,b1,a,b):
    dp[a][b] = 0
    if a== b == N-1:
        dp[a][b] = 1
        return 1
    for i in range(3):
        xa = a + dy[i]
        ya = b + dx[i]
        
        if xa < 0 or ya <0 or xa >= N or ya >= N or graph[xa][ya] == 1: continue
        if a1 == a and b1 != b and i ==2: #오른쪽
            continue
        if a1 !=a and b1 == b and i ==0: #아래 
            continue
        
        if dp[xa][ya] != -1:
            return dp[xa][ya]
        
        dp[a][b] += DFS(a,b,xa,ya)
        
        # case xa가 대각선 
    
    return dp[a][b]

print(DFS(0,0,0,1))