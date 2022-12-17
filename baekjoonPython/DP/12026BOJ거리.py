import sys

input = sys.stdin.readline


N = int(input())

l = list(map(str,input().strip()))

dp =[sys.maxsize]*N
dp[0] = 0

# B에서 O까지 최소 거리 체크
# O에서 J까지 최소거리 체크
# J에서 B까지 최소거리 넣기

for i in range(1,len(l)):
        for j in range(i):
            if l[j] =='B' and l[i] =='O':
                dp[i] =min(dp[i],dp[j]+(j-i)**2)
            if l[j] =='O' and l[i] =='J':
                dp[i] =min(dp[i],dp[j]+(j-i)**2)
            if l[j] =='J' and l[i] =='B':
                dp[i] =min(dp[i],dp[j]+(j-i)**2)
                
if dp[-1] == sys.maxsize:
    print(-1)
else:
    print(dp[-1])