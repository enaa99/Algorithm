import sys

input = sys.stdin.readline

a,b,c = map(int,input().split())

if b >= c:
    print(-1)
    exit(0)

k = c-b

y = a//k + 1
print(y)