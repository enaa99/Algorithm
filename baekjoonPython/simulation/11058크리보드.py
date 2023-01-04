import sys

input = sys.stdin.readline

N = int(input())


dp = [0]*101

for i in range(1,7):
    dp[i] = i


for i in range(7,N+1):
    for j in range(1,N-3):
        dp[i] = max(max(dp[i - 1] + 1, (dp[i - (j+2)] * (j + 1))), dp[i])

print(dp[N])