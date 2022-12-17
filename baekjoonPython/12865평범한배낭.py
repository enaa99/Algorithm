import sys

input = sys.stdin.readline

# N 물품 수 / K 버틸 수 있는 무게 
N,K = map(int,input().split())

dp = [[0]*(K+1) for _ in range(N+1)]

graph = [[0,0]]

for _ in range(N):
    graph.append(list(map(int,input().split())))



for i in range(1,N+1): # 물품
    for j in range(1,K+1): # 무게
        weight = graph[i][0]
        value = graph[i][1]
        
        if j < weight :
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-weight]+value)
print(dp[-1][-1])