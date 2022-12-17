import sys
from collections import deque
input = sys.stdin.readline

K = int(input())

q = deque()
check = False
def BFS(cnt,col):
    global check
    q.append(cnt)
    if color[cnt] == 0:color[cnt] = col
    while q:
        v = q.popleft()
        tmp = color[v]
        for i in l[v]:
            if color[i] == 0:
                color[i] = -tmp
                q.append(i)
            elif color[i] == tmp:
                check = True
                break

for _ in range(K):
    V,E = map(int,input().split())
    l = [[]for _ in range(V+1)]    
    color = [0]*(V+1)
    check = False
    for i in range(E):
        a,b = map(int,input().split())
        l[a].append(b)
        l[b].append(a)
    
    for i in range(1,V+1):
        BFS(i,1)
    if check: print('NO')
    else : print('YES')


