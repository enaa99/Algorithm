import sys

input = sys.stdin.readline

N,M = map(int,input().split())

J = int(input())
cnt = 0
i = 1

pos = M
for _ in range(J):
    k = int(input())
    
    if i <= k <= pos:
        continue
    
    if abs(k-pos) <= abs(k-i):
        cnt += abs(k-pos)
        pos = k
        i = pos-M+1
        
    else:
        cnt += abs(k-i)
        i = k
        pos = i+M-1
    

    
    
print(cnt)