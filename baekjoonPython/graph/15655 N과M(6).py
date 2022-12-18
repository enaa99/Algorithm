import sys

input = sys.stdin.readline

N,M = map(int,input().split())

l = list(map(int,input().split()))

l.sort()

isUsed = [False]*(N+1)

arr = [0]*(N+1)

def DFS(v,cnt):
    if cnt == M:
        for i in range(M):
            print(arr[i],end = " ")
        print()
        return
    for i in range(v,len(l)):
        if not isUsed[i]:
            isUsed[i] = True
            arr[cnt] = l[i]
            DFS(i,cnt+1)
            isUsed[i] = False

DFS(0,0)