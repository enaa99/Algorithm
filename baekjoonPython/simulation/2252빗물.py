import sys
input = sys.stdin.readline

H,W = map(int,input().split())

l = list(map(int,input().split()))

cnt = 0

for i in range(1,W-1):
    le = r = 0
    for j in range(i): le = max(le,l[j])
    for k in range(W-1,i,-1): r = max(r,l[k])
    cnt += max(0,min(le,r)-l[i])
print(cnt)