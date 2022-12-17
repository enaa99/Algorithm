import sys
input = sys.stdin.readline


n = int(input())

dp = [0]*(n+4)

dp[1], dp[2], dp[3] = 1,2,3

for i in range(4,n+1):
    dp[i] = (dp[i-2] + dp[i-1])%15746

print(dp[n])