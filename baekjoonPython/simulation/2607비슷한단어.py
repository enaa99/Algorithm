import sys
from collections import deque

input = sys.stdin.readline

N = int(input())


first = input().rstrip()

f_len = len(first)

ans = 0
q = []
for _ in range(N-1):
    check = list(input().rstrip())
    cnt = 0
    if len(check) == f_len -1:
        for s in first:
            if s in check:
                k = check.index(s)
                check.pop(k)
                cnt += 1
        if cnt == f_len -1:
            ans += 1
    elif len(check) == f_len:
        for s in first:
            if s in check:
                k = check.index(s)
                check.pop(k)
                cnt += 1
        if f_len -1 <= cnt:
            ans +=1
    elif len(check) == f_len + 1:
        for s in first:
            if s in check:
                k = check.index(s)
                check.pop(k)
                cnt += 1
        if f_len -1 < cnt <= f_len +1:
            ans +=1
print(ans)