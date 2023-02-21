import sys

input = sys.stdin.readline

graph = [list(map(int,input().split()))for _ in range(3)]


for i in range(3):
    k = sum(graph[i])
    if k == 0:
        print('D')
    elif k== 1:
        print('C')
    elif k==2:
        print('B')
    elif k==3:
        print('A')
    else:
        print('E')