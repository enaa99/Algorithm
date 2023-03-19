import sys

input = sys.stdin.readline

N = int(input())

# 3,5 최소

# 처음 5를 빼고 5를 뺄 수 있으면 빼고 아니면 3을 빼면서 체크 

def dfs(cnt,v):
    if v == 0:
        print(cnt)
        exit(0)
    elif v<0:
        return
    
    for i in (5,3):
        dfs(cnt+1,v-i)

dfs(0,N)
print(-1)