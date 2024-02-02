import sys
from itertools import product

N, M = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
pos = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
pos = [(x-1, y-1) for x, y in pos]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

moving = []
for a in range(4):
    for b in range(4):
        for c in range(4):
            moving.append((a, b, c))

max_num = 0
for a, b, c in moving:
    for a1, b1, c1 in moving:
        for a2, b2, c2 in moving:
            check = [[0]*N for _ in range(N)]
            tmp = [(a, b, c), (a1, b1, c1), (a2, b2, c2)]
            sum_val = 0
            for p in range(M):
                x, y = pos[p]
                if not check[x][y]:
                    check[x][y] = 1
                    sum_val += graph[x][y]
                for k in range(3):
                    m = tmp[p][k]
                    x += dy[m]
                    y += dx[m]
                    if x < 0 or y < 0 or x >= N or y >= N:
                        break
                    if not check[x][y]:
                        check[x][y] = 1
                        sum_val += graph[x][y]
            max_num = max(max_num, sum_val)

print(max_num)
