import sys

input = sys.stdin.readline


N,S,M = map(int,input().split())
l = list(map(int,input().split()))

# 곡의 개수 N ,시작 볼륨 S , 최대 볼륨 M

def check(p,k):
    if k >=0 and k <=M:
        dp[p][k] = True

dp = [[False]*(M+1) for _ in range(N+1)]


dp[0][S] = True
for i in range(N):   
    for j in range(M+1):
        if dp[i][j]:
            a = j+l[i]
            b = j -l[i]
            check(i+1,a)
            check(i+1,b)
ans = -1
for i in range(M,-1,-1):
    if dp[-1][i]:
        ans = i
        break
print(ans)