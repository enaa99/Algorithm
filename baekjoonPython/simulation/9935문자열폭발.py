import sys
from collections import deque

input = sys.stdin.readline


strings = input().rstrip()

bomb = input().rstrip()

bomb_len = len(bomb)
q = deque()
for i in strings:
    if i == bomb[-1]:
        q.append(i)
        tmp = []
        cnt = 0
        while q:
            tmp.append(q.pop())
            cnt += 1
            if cnt == bomb_len:
                break
        
        if cnt == bomb_len:
            check = ""
            for i in range(len(tmp)-1,-1,-1) :
                check += tmp[i]
            if check == bomb:
                continue
            
        while tmp:
            q.append(tmp.pop())
    else:
        q.append(i)

if q:
    while q:
        print(q.popleft(),end='')
else:
    print('FRULA')