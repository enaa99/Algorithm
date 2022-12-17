import sys
input = sys.stdin.readline

N = int(input())

graph = list(map(int,input().split()))

dp = graph[:]

for i in range(N):
    for j in range(i):
        if graph[i] > graph[j] :
            dp[i] = max(dp[i],dp[j]+graph[i])

print(max(dp))