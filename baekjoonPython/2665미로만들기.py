import sys
from collections import deque
import heapq

input = sys.stdin.readline

n = int(input())

l =[[int(i) for i in input().strip()]for _ in range(n)]
isUsed = [[False for _ in range(n)]for i in range(n)]


dx = [1,0,-1,0]
dy = [0,-1,0,1]


def BFS(start):
    q = []
    heapq.heappush(q,start)
    while q:
        z,x,y = heapq.heappop(q)
        for i in range(4):
            xa = x + dx[i]
            ya = y + dy[i]
            if xa == n-1 and ya == n-1:
                print(z)
                q = []
                break
            if xa <0 or xa>=n or ya<0 or ya>=n: continue
            if isUsed[xa][ya]: continue
            isUsed[xa][ya] = True
            if l[xa][ya] == 0:
                heapq.heappush(q,((z+1,xa,ya)))
            else:
                heapq.heappush(q,((z,xa,ya)))
    
BFS((0,0,0))
