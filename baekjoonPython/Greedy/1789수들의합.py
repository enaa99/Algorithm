import sys

input = sys.stdin.readline

s = int(input())

# 서로 다른 N개의 자연수의 합 = S

n = 1
while n * (n + 1) / 2 <= s:
    n += 1
print(n - 1)