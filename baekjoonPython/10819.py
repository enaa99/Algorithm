import sys


n = int(sys.stdin.readline())

k = list(map(int,sys.stdin.readline().split()))


isUsed = [0]*n
l=[0]*n
ans = 0

def DFS(cnt):
    global ans
    tmp =0
    if cnt == n:
        for i in range(2,len(l)+1):
            tmp += abs(l[i-2] -l[i-1])
        
        ans = max(ans,tmp)
        return
    
    for i in range(n):
        if not isUsed[i]:
            l[cnt] = k[i]
            isUsed[i] = True
            DFS(cnt+1)
            isUsed[i] = False

DFS(0)
print(ans)