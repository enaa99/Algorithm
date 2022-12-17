import sys

input = sys.stdin.readline

n,m = map(int,input().split())

l =[[]for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    l[a].append(b)
    l[b].append(a)

q = []
isUsed =[False]*(n+1)
ans = 0
def BFS(cnt):
    if not isUsed[cnt]:
        global ans
        ans +=1
        q.append(cnt)
        isUsed[cnt] = True
        while q:
            v = q.pop(0)
            for i in l[v]:
                if not isUsed[i]:
                    isUsed[i] = True
                    q.append(i)
                    
for i in range(1,n+1):
    BFS(i)
print(ans)