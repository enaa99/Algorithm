import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
###DFS
n = int(input())
isUsed =[False]*(n+1)
tree = [[]for i in range(n+1)]

for i in range(n-1):
    a,b = map(int,input().split())
    tree[b].append(a)
    tree[a].append(b)

ans = [0]*(n+1)

def DFS(cnt):
    for i in tree[cnt]:
        if not isUsed[i] : 
            ans[i] = cnt
            isUsed[i] = True
            DFS(i)

#DFS(1)

q =[]
def BFS(cnt):
    q.append(cnt)
    isUsed[cnt] = True
    while q:
        v= q.pop(0)
        for i in tree[v]:
            if not isUsed[i]:
                isUsed[i] = True
                ans[i] = v
                q.append(i)
BFS(1)
for i in range(2,len(ans)):
    print(ans[i])