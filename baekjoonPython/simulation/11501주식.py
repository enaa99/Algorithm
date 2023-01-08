import sys

input = sys.stdin.readline

T = int(input())

for i in range(T):
    k = int(input())
    days = list(map(int,input().split()))
    
    dp = [0]*(len(days))
    for j in range(1,len(days)):
        for u in range(j-1,-1,-1):
            if days[j] > days[u]:
                dp[j] += days[j]-days[u]
            else:
                # days[j] < days[u]
                dp[j] += dp[u]
                break
    print(dp[-1])