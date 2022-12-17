import sys

input = sys.stdin.readline

ans1 = sys.maxsize
ans2 = -sys.maxsize
# 식의 결과가 최대 최소 인 것을 구하기.....


# ==== +, -, x, %  -> 순서


# 수의 개수
N = int(input())

l = list(map(int,input().split()))

k = list(map(int,input().split()))


def dfs(cnt,ans,plus,minus,mul,div):
    global ans1,ans2
    if cnt == N:ans1 = min(ans1,ans);ans2 = max(ans2,ans);return
    if plus: dfs(cnt+1,ans+l[cnt],plus-1,minus,mul,div)
    if minus: dfs(cnt+1,ans-l[cnt],plus,minus-1,mul,div)
    if mul: dfs(cnt+1,ans*l[cnt],plus,minus,mul-1,div)    
    if div:
        ans = ans//l[cnt] if ans>0 else -(-ans//l[cnt])
        dfs(cnt+1,ans,plus,minus,mul,div-1)    
    
dfs(1,l[0],k[0],k[1],k[2],k[3])
print(ans2,ans1,sep='\n')
