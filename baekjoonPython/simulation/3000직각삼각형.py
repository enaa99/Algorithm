import sys

input =sys.stdin.readline


N = int(input())

def fib(n):
    if(n==1 or n==2):
        return 1
    else:
        return(fib(n-1)+fib(n-2))

dp = [0]*(N+3)
dp[0],dp[1],dp[2],dp[3] = 0,1,1,2

for i in range(4,N+1):
    dp[i] = dp[i-2] + dp[i-1]

