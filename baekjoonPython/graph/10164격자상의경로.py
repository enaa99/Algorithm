import sys
from collections import deque

input = sys.stdin.readline


N,M,K = map(int,input().split())


dx = [1,0]
dy = [0,1]

dp = [[0]*(M+1) for _ in range(N+1)]

def search():
    cnt = 1
    for i in range(N):
        for j in range(M):
            if cnt == K:
                return i+1,j+1
            cnt +=1

def dynaminc(x,y,dest):
    for i in range(x,dest[0]+1):
        for j in range(y,dest[1]+1):
            dp[i][j] += dp[i-1][j] + dp[i][j-1]

dp[1][1] = 1

if K!=0:
    a,b = search()
    dynaminc(1,1,(a,b))
    x = dp[a][b]
    dp = [[0]*(M+1) for _ in range(N+1)]
    dp[a][b] = x
    dynaminc(a,b,(N,M))
    print(dp[-1][-1])
else:
    dynaminc(1,1,(N,M))
    print(dp[-1][-1])


# def BFS(a,b,dest):
#     ans = 0
#     q = deque()
#     q.append((a,b))
    
#     while q:
#         x,y = q.popleft()
#         if x == dest[0] and y == dest[1]:
#             ans += 1
#             continue
        
#         for i in range(2):
#             xa = x + dx[i]
#             ya = y + dy[i]
            
            
#             if xa < 0 or ya < 0 or xa>dest[0] or ya>dest[1] : continue
            
#             q.append((xa,ya))
            
#     return ans

# def DFS(a,b,dest):
#     if a == dest[0] and b == dest[1]:
#         return 1
#     for i in range(2):
#         xa = a + dx[i]
#         ya = b + dy[i]
#         if xa < 0 or ya < 0 or xa>dest[0] or ya>dest[1] : continue
#         if graph[xa][ya] !=0:
#             graph[a][b] += graph[xa][ya]
#             return graph[a][b]
#         graph[a][b] += DFS(xa,ya,dest)
#     return graph[a][b]

# def search():
#     cnt = 1
#     for i in range(N):
#         for j in range(M):
#             if cnt == K:
#                 return i,j
#             cnt +=1

# if K == 0:
#     print(DFS(0,0,(N-1,M-1)))
# else:
#     a,b = search()
#     x = DFS(0,0,(a,b))
#     graph[a][b] = 0   
#     y = DFS(a,b,(N-1,M-1))
#     print(x*y)

