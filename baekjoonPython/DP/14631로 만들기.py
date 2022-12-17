import sys

input = sys.stdin.readline

n = int(input())

dp =[sys.maxsize]*(n+5)

dp[1],dp[2],dp[3],dp[4] = 0,1,1,2


for i in range(5,n+1):
    if i%3 ==0:
        dp[i] = dp[i//3]+1
    if i%2 == 0:
        dp[i] = min(dp[i],dp[i//2]+1)
    
    dp[i] = min(dp[i],dp[i-1]+1)

print(dp[n])
