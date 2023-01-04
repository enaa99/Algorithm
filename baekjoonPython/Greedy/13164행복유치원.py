import sys

input = sys.stdin.readline

N,K = map(int,input().split())

childs = list(map(int,input().split()))


# 큰 것들은 한개
# 작은 것들 끼리

tmp = []

for i in range(1,N):
    tmp.append(childs[i]-childs[i-1])

tmp.sort()

ans = 0
for i in range(N-K):
    ans += tmp[i]

print(ans)
