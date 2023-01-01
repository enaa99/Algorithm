import sys
from collections import deque

input = sys.stdin.readline


# N, M, x, y, K
# 세로 가로 좌표 명령개수


N, M, x, y, k = map(int, input().split())

board = []

dx = [0,0, 0, -1, 1]
dy = [0,1, -1, 0, 0]
dice = [0, 0, 0, 0, 0, 0]

def move(dir):
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if dir == 1: #동
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, b, a, f, e, c

    elif dir == 2: #서
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, f, a, e, d

    elif dir == 3: #북
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, a, c, d, f, b

    else:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, c, d, a, e

for i in range(N):
    board.append(list(map(int, input().split())))

dices = list(map(int, input().split()))

nx, ny = x, y
for i in dices:
    nx += dx[i]
    ny += dy[i]

    if nx < 0 or ny < 0 or nx >= N  or ny >= M:
        nx -= dx[i]
        ny -= dy[i]
        continue
    
    move(i)
    
    if board[nx][ny] == 0:
        board[nx][ny] = dice[-1]
    else:
        dice[-1] = board[nx][ny]
        board[nx][ny] = 0

    print(dice[0])