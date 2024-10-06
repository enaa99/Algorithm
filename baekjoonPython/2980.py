import sys

input = sys.stdin.readline

N, L = map(int, input().split())

# 1초에 1미터


pos = 0
answer = 0

for _ in range(N):
    d, r, g = map(int, input().split())

    answer += (d - pos)
    pos = d
    if answer % (r+g) <= r:
        answer += (r - (answer%(r+g)))
answer += L - pos
print(answer)