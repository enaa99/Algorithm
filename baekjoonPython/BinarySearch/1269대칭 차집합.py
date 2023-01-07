import sys
from bisect import bisect_left

input = sys.stdin.readline

N,M = map(int,input().split())

a = list(map(int,input().split()))

b = list(map(int,input().split()))

a.sort()

cnt = 0 

for j in range(M):
    k = bisect_left(a,b[j])
    
    if k < N and a[k] == b[j]:
        cnt +=1
        

print(N+M-2*cnt)