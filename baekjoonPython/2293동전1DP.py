import sys

input = sys.stdin.readline


a,b = map(int,input().split())

l = [int(input()) for _ in range(a)]

dp = [0]*(b+1)
dp[0] = 1



for coin in l:
    for i in range(b+1):
        if i>=coin:
            dp[i] += dp[i-coin]

print(dp[b])