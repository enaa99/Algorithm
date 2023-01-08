import sys
input = sys.stdin.readline

count = 0
def DFS(x,y):
    global count
    count += 1
    if y == C-1:
        return True
    for d in dx:

        xa = x+d
        
        if xa<0 or xa>=R or graph[xa][y+1] =='x'or isUsed[xa][y+1]: continue

        isUsed[xa][y+1] = 1
        if DFS(xa, y+1):
            return True
    return False

R, C = map(int,input().split())

isUsed = [[0]*C for _ in range(R)]

graph = [list(map(str,input().rstrip())) for _ in range(R)]

dx = [-1,0,1]
ans = 0
for i in range(R):
    if DFS(i,0):
        ans+=1

print(ans)