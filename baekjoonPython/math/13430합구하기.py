import sys

input = sys.stdin.readline

k,n = map(int,input().split())

memo ={}
# dp =[[0]*(n+1) for _ in range(k+1)]

# def pro(a,b):
#     if a ==0:
#         return b
#     if dp[a][b] != 0:
#         return dp[a][b]
    
#     for i in range(1,b+1):
#         dp[a-1][i] = pro(a-1,i)
#         dp[a][b] += dp[a-1][i]
        
#     return dp[a][b]%1000000007


def program(a,b):
    if not memo.get(f'{a},{b}'):
        memo[f'{a},{b}'] =0
    
    if a == 0:
        return b
    if memo[f'{a},{b}'] != 0:
        return memo[f'{a},{b}']
    
    for i in range(1,b+1):
        memo[f'{a-1},{i}'] = program(a-1,i)
        memo[f'{a},{b}'] += memo[f'{a-1},{i}']
    return memo[f'{a},{b}']%1000000007

print(program(k,n))

