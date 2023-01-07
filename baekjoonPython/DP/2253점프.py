import sys
sys.setrecursionlimit(10**5)

input = sys.stdin.readline

N,M = map(int,input().split())

# M은 점프할 수 없는 돌

small = [int(input()) for _ in range(M)]

dp = [sys.maxsize]*(N+1)


dp[1] = 0


# 점프는 k-1,k,k+1 
def jump(k,v):
    if k+v> N or k >N or k+v+1 >N: return
    
    if v != 1 and k+v-1 not in small:
        dp[k+v-1] = min(dp[k+v-1],dp[k] + 1)
        jump(k+v-1,v-1)
    if k+v not in small:
        dp[k+v] = min(dp[k+v],dp[k]+1)
        jump(k+v,v)
    if k+v+1 not in small:
        dp[k+v+1] = min(dp[k]+1,dp[k+v+1])
        jump(k+v+1,v+1)

jump(1,1)

if dp[N] != sys.maxsize:
    print(dp[N])
else:
    print(-1)