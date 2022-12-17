import sys


input = sys.stdin.readline


a,b = map(int,input().split())


def DFS(value,cnt):
    if value < a and a!=b:
        print(-1)
        exit(0)
    elif value == a:
        print(cnt)
        exit(0)
    
    
    if value%10 == 1:
        DFS(value//10,cnt+1)
    elif value%2 !=0:
        print(-1)
        exit(0)
    else:
        DFS(value//2,cnt+1)

DFS(b,1)
