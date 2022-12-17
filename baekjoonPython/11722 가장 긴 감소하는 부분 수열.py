import sys
input = sys.stdin.readline

N = int(input())
l = list(map(int,input().split()))
dp = [1]*N
for i in range(N-1,-1,-1):
    for j in range(N-1,i,-1):

        if l[i] > l[j] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1

print(max(dp))
