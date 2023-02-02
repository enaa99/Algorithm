import sys
from collections import deque


input = sys.stdin.readline


q = deque()

for _ in range(int(input())):
    k = input().split()
    
    if k[0] == "push_back":
        q.append(k[1])
    elif k[0] == "push_front":
        q.appendleft(k[1])
    elif k[0] == "front":
        if q:
            print(q[0])
        else:
            print(-1)
    elif k[0] == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)
    elif k[0] == 'size':
        print(len(q))
    elif k[0] == 'empty':
        if not q:
            print(1)
        else:
            print(0)
    elif k[0] == 'pop_front':
        if q:
            print(q.popleft())
        else:
            print(-1)
    else:
        if q:
            print(q.pop())
        else:
            print(-1)