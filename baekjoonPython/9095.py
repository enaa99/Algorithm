import sys

def DFS(cnt,val):
    
    global ans
    
    if val == n:
        ans +=1
        return
    for i in range(1,4):
        val += i
        if val <= n:
            DFS(cnt+1,val)
            val -= i

# for _ in range(int(sys.stdin.readline())):
#     n = int(sys.stdin.readline())
#     ans =0
#     DFS(0,0)
#     print(ans)
    

############################### DP
input = sys.stdin.readline
t = int(input())
dp = [0]*12
dp[1],dp[2],dp[3] = 1,2,4

for i in range(4,12):
    dp[i] = dp[i-1]+dp[i-2] + dp[i-3]
    
for _ in range(t):
    n = int(input())
    print(dp[n])



# DP






