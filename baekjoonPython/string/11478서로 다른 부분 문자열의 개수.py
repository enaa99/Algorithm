import sys

input = sys.stdin.readline

S = list(input().rstrip())

# ababc
# a,b,c,ab,ba,bc,aba,bab,abc,abab,babc,ababc

len_s = len(S)
check = set()


def dfs(v,k):
    if v:
        check.add(v)
    if k >= len_s: return
    
    dfs(v+S[k],k+1)

for i in range(len(S)):
    dfs(S[i],i+1)

print(len(check))