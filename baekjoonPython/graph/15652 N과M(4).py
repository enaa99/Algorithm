import sys

input = sys.stdin.readline

N,M = map(int,input().split())

arr = [0]*(N+1)
isUsed = [False]*(N+1)

def DFS(v,cnt):
    if cnt == M:
        for i in range(M):
            print(arr[i],end=" ")
        print()
        return
    for i in range(v,N+1):
            arr[cnt] = i
            DFS(i,cnt+1)

DFS(1,0)