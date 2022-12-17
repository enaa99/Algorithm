import sys
input = sys.stdin.readline

N = int(input())

dp = [0]*(N+2)


graph = [(0,0)]
for _ in range(N):
    a,b = map(int,input().split())
    graph.append((a,b))

check = 0
for i in range(N,0,-1):
    
    if i + graph[i][0] > N+1:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1],graph[i][1]+dp[i+graph[i][0]])

print(dp[1])