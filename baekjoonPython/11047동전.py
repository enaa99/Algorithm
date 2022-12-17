import sys
from collections import deque
input = sys.stdin.readline

N,K = map(int,input().split())

# 동전 개수의 최소값

l = deque()
for _ in range(N):
    l.append(int(input()))

cnt = 0
for i in range(len(l)-1,-1,-1):
    cnt += K//l[i]
    K %= l[i]
print(cnt)