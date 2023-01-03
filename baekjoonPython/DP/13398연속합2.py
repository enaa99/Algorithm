import sys

input = sys.stdin.readline


N = int(input())

numbers = list(map(int,input().split()))

dp = [[0] * N for _ in range(2)]

dp[0][0] = numbers[0] 

if N > 1:
    ans = -sys.maxsize
    
    for i in range(1, N):
        dp[0][i] = max(dp[0][i - 1] + numbers[i], numbers[i])
        dp[1][i] = max(dp[0][i - 1], dp[1][i-1] + numbers[i])

        ans = max(ans, dp[0][i], dp[1][i])
    print(ans)
else: 
    print(dp[0][0])