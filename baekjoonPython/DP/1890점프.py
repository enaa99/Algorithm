import sys
input = sys.stdin.readline


n = int(input())
l = [list(map(int,input().split())) for _ in range(n)]

dp =[[0]*n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if l[i][j] == 0:break
        
        if j + l[i][j] < n :
            dp[i][j+l[i][j]] += dp[i][j]
        
        if i + l[i][j] < n :
            dp[i+l[i][j]][j] += dp[i][j]

print(dp[-1][-1])