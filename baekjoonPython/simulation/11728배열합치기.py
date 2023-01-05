import sys

input = sys.stdin.readline

N,M = map(int,input().split())

A = list(map(int,input().split()))

B = list(map(int,input().split()))


for i in B:
    A.append(i)

A.sort()

print(*A)