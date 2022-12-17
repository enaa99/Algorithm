import sys
from collections import deque
input = sys.stdin.readline


# N 세로 길이, M 가로 길이, 음식물 쓰레기의 개수 K

N,M,K = map(int,input().split())

l=[[0 for _ in range(M)]for i in range(N)]

for _ in range(K):
    a,b = map(int,input().split())
    l[a-1][b-1] = 1


isUsed = [[False for _ in range(M)]for i in range(N)]

dx = [1,0,-1,0]
dy = [0,-1,0,1]

q = deque()
def BFS(start):
    cnt = 1
    q.append(start)
    isUsed[start[0]][start[1]] = True
    while q:
        x,y = q.popleft()
        for i in range(4):
            xa = x +dx[i]
            ya = y+ dy[i]
            
            if xa < 0 or ya<0 or xa>=N or ya>=M: continue
            if l[xa][ya] == 0 or isUsed[xa][ya]: continue
            
            isUsed[xa][ya] = True
            q.append((xa,ya))
            cnt +=1
    return cnt

answer = 0
for i in range(N):
    for j in range(M):
        if not isUsed[i][j] and l[i][j] == 1:
            answer = max(BFS((i,j)),answer)

print(answer)