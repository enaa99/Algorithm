import sys


n,m = map(int,sys.stdin.readline().split())

isUsed =[0]*n
arr = [0]*n

def BFS(cnt):
    if cnt == m:
        for i in range(m):
            print(arr[i],end=' ')
        print()
    else:
        for i in range(1,n+1):
            arr[cnt] = i
            BFS(cnt+1)


BFS(0)