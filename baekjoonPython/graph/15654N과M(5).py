import sys

input = sys.stdin.readline

N,M = map(int,input().split())

l = list(map(int,input().split()))
l.sort()
arr = [0]*(N+1)
isUsed = [False]*(N+1)
def DFS(cnt):
    if cnt == M:
        for i in range(M):
            print(arr[i],end=" ")
        print()
        return
    
    for i in range(len(l)):
        if not isUsed[i]:
            arr[cnt] = l[i]
            isUsed[i] = True
            DFS(cnt+1)
            isUsed[i] = False

DFS(0)