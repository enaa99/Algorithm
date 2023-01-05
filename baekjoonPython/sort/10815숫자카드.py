import sys
from bisect import bisect_left

input = sys.stdin.readline

N = int(input())
mine = list(map(int,input().split()))

M = int(input())
others = list(map(int,input().split()))

mine.sort()

for num in range(len(others)):
    k = bisect_left(mine,others[num])
    if k <= len(mine)
        if mine[k] == others[num]:
            others[num] = 1
            continue
    
    others[num] = 0

print(*others)