import sys
import copy
input = sys.stdin.readline

N,M = map(int,input().split())


graph = [list(map(int,input().split())) for i in range(N)]

minV = [sys.maxsize]

cctv = []
mode = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]],
]

# 북 - 동 - 남 - 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]



for i in range(N):
    for j in range(M):
        if graph[i][j] in [1,2,3,4,5]:
            cctv.append([graph[i][j],i,j])


def fill(board,mm,x,y):
    
    for i in mm:
        nx,ny = x, y
        while True:
            nx += dx[i]
            ny += dy[i]
            
            if nx < 0 or ny < 0 or nx >= N or ny>= M : break
            
            if board[nx][ny] == 6: break
            
            if board[nx][ny] == 0:
                board[nx][ny] = -1
    
    return



def dfs(depth,arr):
    if minV[0] == 0:
        return
    
    if depth == len(cctv):
        cnt = 0
        for i in range(N):
            cnt += arr[i].count(0)
        minV[0] = min(minV[0],cnt)
        return
    tmp = copy.deepcopy(arr)
    num_cctv,a,b = cctv[depth]
    for i in mode[num_cctv]:
        fill(tmp,i,a,b)
        dfs(depth+1,tmp)
        tmp = copy.deepcopy(arr)

dfs(0,graph)

print(minV[0])