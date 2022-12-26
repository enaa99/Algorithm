import sys

input = sys.stdin.readline

n,k = map(int,input().split())

coins = [int(input()) for _ in range(n)]

dp =[0]*(k+1)

for i in range(1,k+1):
    a = []
    for coin in coins:
        if coin <=i and dp[i-coin] != -1:
            a.append(dp[i-coin])
    if not a:
        dp[i] = -1
    else:
        dp[i] = min(a) + 1

print(dp[k])