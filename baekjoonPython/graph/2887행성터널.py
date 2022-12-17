import sys
input = sys.stdin.readline

N = int(input())


graph = [list(map(int,input().split())) for _ in range(N)]

parent = [i for i in range(N+1)]

def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]

def union(a,b):
    ra = find(a)
    rb = find(b)
    
    if ra > rb : parent[ra] = rb
    else: parent[rb] = ra

l = [[sys.maxsize for i in range(N)] for _ in range(N)]

for i in range(N):
    tmp = sys.maxsize
    for j in range(N):        
        if i != j:
            k = min(abs(graph[i][0]-graph[j][0]),abs(graph[i][1]-graph[j][1]),abs(graph[i][2]-graph[j][2]))
            tmp = min(tmp,k)
            l[i][j] = min(l[i][j],tmp)
        else:
            l[i][j] = 0







