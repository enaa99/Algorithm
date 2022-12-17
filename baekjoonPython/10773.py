import sys

input = sys.stdin.readline

s = []
for _ in range(int(input())):
    k = int(input())
    if k != 0:
        s.append(k)
    else:
        s.pop()

print(sum(s))