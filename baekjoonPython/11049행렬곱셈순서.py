import sys

input = sys.stdin.readline

N = int(input())

graph = [list(map(int,input().split())) for _ in range(N)]

dp = [[0]*N for _ in range(N)]

for k in range(N):
    for i in range(N-k):
        j = i+k
        if i == j: continue
        dp[i][j] = sys.maxsize
        for p in range(i,j):
            dp[i][j] = min(dp[i][j], dp[i][p] + dp[p+1][j] + graph[i][0]*graph[p][1]*graph[j][1])

print(dp[0][-1])