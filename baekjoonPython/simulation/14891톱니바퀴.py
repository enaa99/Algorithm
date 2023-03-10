import sys
from collections import deque

input = sys.stdin.readline

graph = []


for _ in range(4):
    
    graph.append(list(deque(int,input().split())))

K = int(input())

# 시계방향 왼쪽으로 한칸 / 반시계방향 오른쪽으로 한칸
# N 극 0, S극 1


for _ in range(K):
    a,b = map(int,input().split())
    
    if b == 1: # 시계방향
        graph[a-1]
        
    else: # 반시계
        
        
        continue