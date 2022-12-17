import sys

n,m = map(int,sys.stdin.readline().split())

isUsed = [False]*n
arr =[0]*n

def DFS(cnt):
    if cnt == m:
        for i in range(m):
            print(arr[i],end=" ")
        print()
        return

    for i in range(1,n+1):
        if(isUsed[i] == False):
            isUsed[i] = True
            arr[cnt] = i
            DFS(cnt+1)
            isUsed[i] = False
            

DFS(0)