import sys

input = sys.stdin.readline

N,K = map(int,input().split())

coins = [int(input()) for _ in range(N)]

dp = [0]*(K+1)

for i in range(1,K+1):
    a =[]
    for coin in coins:
        if coin <= i and dp[i-coin] != -1:
            a.append(dp[i-coin])
    
    if not a:
        dp[i] = -1
    else:
        dp[i] = min(a)+1
        