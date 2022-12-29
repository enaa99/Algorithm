import sys

input = sys.stdin.readline

N = int(input())

queens = [0]*N

ans = 0

def check(k):
    for i in range(k):
        if queens[i] == queens[k] or abs(k-i) == abs(queens[k]-queens[i]):
            return False
    return True

def DFS(cnt):
    global ans
    if cnt == N:
        ans +=1
        return 
    
    for i in range(N):
        queens[cnt] = i
        if check(cnt):
            DFS(cnt+1)
DFS(0)
print(ans)

