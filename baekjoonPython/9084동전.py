import sys
input = sys.stdin.readline

# T 테스트케이스
T = int(input())

for _ in range(T):
    n = int(input()) #동전 종류
    coins = list(map(int,input().split()))
    price = int(input())
    
    dp =[0]*(price+1)
    dp[0] = 1
    for coin in coins:
        for i in range(price+1):
            if i  >= coin:
                dp[i] += dp[i-coin]
    print(dp[price])