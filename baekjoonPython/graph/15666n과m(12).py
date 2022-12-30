import sys

input = sys.stdin.readline

N,M = map(int,input().split())

graph = list(map(int,input().split()))

graph.sort()

arr = [0]*N

def DFS(cnt,v):
    if cnt == M:
        for i in range(M):
            print(arr[i],end=" ")
        print()
        return

    end = -1
    for i in range(v,N):
        if graph[i] != end:
            end = graph[i]
            arr[cnt] = graph[i]
            DFS(cnt+1,i)

DFS(0,0)