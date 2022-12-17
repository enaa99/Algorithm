import sys

input = sys.stdin.readline

N = int(input())
dp = [0]*(N+2)

l = [(0,0)]
for _ in range(N):
    a,b = map(int,input().split())
    l.append((a,b))
    

for i in range(len(l)-1,0,-1):
    if l[i][0] + i > N+1:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1],l[i][1] + dp[i+l[i][0]]) 
        
print(dp[1])