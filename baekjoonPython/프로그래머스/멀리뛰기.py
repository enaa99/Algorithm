def solution(n):
    
    dp = [0]*(n+3)
    
    # 1칸 또는 2칸 점프 가능 n번째 칸까지 가야된다.
    dp[1] = 1
    dp[2] = 2
    
    
    for i in range(3,n+1):
        dp[i] = (dp[i-1] + dp[i-2])%1234567
    
    return dp[n]