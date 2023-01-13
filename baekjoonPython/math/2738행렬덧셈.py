import sys

input = sys.stdin.readline

a,b = map(int,input().split())

A = [list(map(int,input().split())) for _ in range(a)]

B = [list(map(int,input().split())) for _ in range(a)]

for i in range(a):
    for j in range(b):
        A[i][j] += B[i][j]

for i in range(a):
    print(*A[i],sep=' ')
