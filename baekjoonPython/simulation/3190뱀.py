import sys
from collections import deque
input = sys.stdin.readline


N = int(input())

graph =[[-1]*(N+1) for _ in range(N+1)]

K = int(input())

for _ in range(K):
    a,b = map(int,input().split())
    graph[a][b] = 1

move = {}
for _ in range(int(input())):
    a,v = map(str,input().split())
    move[a] = v

dx = [1,0,-1,0]
dy = [0,-1,0,1]
q = deque()
q.append((1,1))
x = y = 1
i = 0
# 직진만 한다
def turn(k):
    if move.get(f'{k}'):
        return True
    return False

cnt = 0
while True:

    x += dx[i]
    y += dy[i]
    cnt +=1
    
    if x <=0 or y <=0 or x>N or y>N or (y,x) in q:
        print(cnt)
        exit(0)
    
    q.appendleft((y,x))
    
    if graph[y][x] == 1:
        graph[y][x] = -1
        
    
    elif graph[y][x] == -1:
        q.pop()
        
    if turn(cnt):
        if move[f'{cnt}'] == 'D':
            i = (i-1)%4
        else:
            i = (i+1)%4

