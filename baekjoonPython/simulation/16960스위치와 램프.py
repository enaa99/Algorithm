import sys

input = sys.stdin.readline

# 스위치 수 N , 램프 수 M

N,M = map(int,input().split())


l = [list(map(int,input().split())) for _ in range(N)]


for i in range(N):
    dp = [0]*(M+1)
    for j in range(N):
        if i == j: continue
        
        for k in range(1,len(l[j])):
            dp[l[j][k]] +=1
    
    if min(dp[1:]) != 0:
        print(1)
        exit(0)
print(0)