import sys
from collections import deque

input = sys.stdin.readline


line1 = list(input().rstrip())
line2 = deque()

N = int(input())

cmd = len(line1)
for _ in range(N):
    k = list(map(str,input().split()))
    
    if len(k) > 1:
        q = []
        line1.append(k[1])
        # for i in range(len(line1)-1,cmd-1,-1):
        #     q.append(line1.pop())
        # line1.append(k[1])
        # while q:
        #     line1.append(q.pop())
        cmd += 1
    else:
        if k[0] == 'L':
            if cmd > 0:
                line2.appendleft(line1.pop())
                cmd -= 1
        elif k[0] == 'D':
            if cmd < len(line1)+len(line2):
                line1.append(line2.popleft())
                cmd += 1
        else:
            if cmd > 0:
                line1.pop()
                cmd -=1

print(*line1, sep='',end='')
print(*line2,sep='')