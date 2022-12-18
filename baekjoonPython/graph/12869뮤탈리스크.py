import sys
from itertools import permutations


input = sys.stdin.readline

N = int(input())

units =list(map(int,input().split()))

dp = [[[100] * (max(units) + 1) for i in range((max(units) + 1))] for j in range((max(units) + 1))]


attack = [9,3,1]
ans = sys.maxsize

def answer(x, y, z, cnt):
    global ans
    if x <= 0 and y <= 0 and z <= 0:
        ans = min(ans,cnt)
        return

    x = 0 if x <= 0 else x
    y = 0 if y <= 0 else y
    z = 0 if z <= 0 else z

    if dp[x][y][z] <= cnt and dp[x][y][z] != 0:
        return

    dp[x][y][z] = cnt

    for i in permutations(attack, 3):
        answer(x - i[0], y - i[1], z - i[2], cnt + 1)

while len(units) < 3:
    units.append(0)

answer(units[0],units[1],units[2],0)

print(ans)