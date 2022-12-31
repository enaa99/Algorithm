import sys

input = sys.stdin.readline


# N -> 웅덩이 // L -> 널빤지 길이
N,L = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(N)]
graph.sort()

cnt = 0
j = 0

for holes in graph:
    start,end = holes[0],holes[1]
    if j< start:
        j = start-1
    
    while j< end-1:
        cnt += 1
        j += L

print(cnt)