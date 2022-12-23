import sys

input = sys.stdin.readline

N,M = map(int,input().split())

l = list(map(int,input().split()))

l.sort()

arr = [0]*(N+1)

def DFS(cnt):
    if cnt == M:
        for i in range(M):
            print(arr[i],end=" ")
        print()
        return
    last = 0
    for i in range(N):
        if last != l[i]:
            last = l[i]
            arr[cnt] = l[i]
            DFS(cnt+1)
            
            
DFS(0)