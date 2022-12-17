import sys

n,m = map(int,sys.stdin.readline().split())

isUsed = [False]*9
arr =[0]*9

def DFS(cnt,num):
    if cnt == m:
        for i in range(m):
            print(arr[i],end=" ")
        print()
        return

    for i in range(num,n+1):
        if(isUsed[i] == False):
            isUsed[i] = True
            arr[cnt] = i
            DFS(cnt+1,i+1)
            isUsed[i] = False
            
DFS(0,1)