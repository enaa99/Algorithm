import sys
from collections import deque

input = sys.stdin.readline

L,W = map(int,input().split())

graph = [list(map(str,input().rstrip())) for _ in range(L)]

def BFS(a,b):
    distance = [[-1]*W for _ in range(L)]
    
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    
    distance[a][b] = 0
    dist = 0
    q = deque()
    q.append([a,b,0])
    while q:
        x,y,dist = q.popleft()
        for i in range(4):
            xa = x + dx[i]
            ya = y + dy[i]
            
            if xa < 0 or ya < 0 or xa>=L or ya>=W : continue
            if graph[xa][ya] == 'W': continue
            
            if distance[xa][ya] == -1 :
                distance[xa][ya] = dist + 1
                q.append([xa,ya,dist+1])
    
    return dist



# 최단 거리로 이동 이분 탐색!!!!
# 최소 부터 계산해서 체크하기
answer = 0
def check():
    global answer
    for i in range(L):
        for j in range(W):
            if graph[i][j] == 'L':
                answer = max(BFS(i,j), answer)
                    
check()

print(answer)
# l = 0
# r = L*W

# while l + 1< r:
#     mid = (l+r)//2
    
#     if check(mid):
#         l = mid
#     else:
#         r = mid

# print(l)
