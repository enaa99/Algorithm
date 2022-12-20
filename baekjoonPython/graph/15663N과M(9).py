import sys

input = sys.stdin.readline

N,M = map(int,input().split())

l = list(map(int,input().split()))

isUsed =[False]*N
arr = [0]*N

l.sort()


def DFS(cnt):
    if cnt == M:
        for i in range(M):
            print(arr[i],end =" ")
        print()
    
    last = 0
    for i in range(len(l)):
        if not isUsed[i] and l[i] != last:
            isUsed[i] = True
            last = l[i]
            arr[cnt] = l[i]
            DFS(cnt+1)
            isUsed[i] = False

DFS(0)