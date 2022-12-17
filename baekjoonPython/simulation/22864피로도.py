import sys

input = sys.stdin.readline


a,b,c,m = map(int,input().split())


day = 0
tmp = 0
ans = 0
while day + 1 <= 24:
    day += 1
    tmp += a
    if tmp > m:
        tmp -= a
        tmp -= c
        tmp = tmp if tmp>=0 else 0
    else:
        ans += b

print(ans)