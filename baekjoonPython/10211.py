import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    lists = list(map(int,input().split()))
    
    dp = [0]*len(lists)
    
    dp[0] = lists[0]
    for i in range(1,len(lists)):
        dp[i] = max(lists[i], dp[i-1] + lists[i])
    
    print(max(dp))
