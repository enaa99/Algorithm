import sys

input = sys.stdin.readline
q= []
n = int(input())
k =int(input())
isUsed =[False]*(n+1)
l = [[] for _ in range(n+1)]
def BFS(cnt):
    q.append(cnt)
    ans = 0
    isUsed[cnt] = True
    while q:
        v = q.pop(0)
        for i in l[v]:
            if not isUsed[i]:
                isUsed[i] = True
                ans +=1
                q.append(i)
    return ans

for _ in range(k):
    a,b = map(int,input().split())
    l[a].append(b)
    l[b].append(a)

print(BFS(1))
