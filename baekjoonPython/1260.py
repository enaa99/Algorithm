import sys

input = sys.stdin.readline


a,b,c = map(int,input().split())

l = [[]for _ in range(a+1)]

for _ in range(b):
    n,m = map(int,input().split())
    l[n].append(m)
    l[m].append(n)

isUsed = [False]*(a+1)
def DFS(cnt):
    for i in sorted(l[cnt]):
        if not isUsed[i]:
            isUsed[i] = True
            print(i,end=' ')
            DFS(i)

q =[]
def BFS(cnt):
    q.append(cnt)
    while q:
        v = q.pop(0)
        print(v,end=' ')
        for i in sorted(l[v]):
            if not isUsed[i]:
                q.append(i)
                isUsed[i] = True

isUsed[c] = True
print(c,end=' ')
DFS(c)
isUsed = [False]*(a+1)
print()
isUsed[c] = True
BFS(c)
