import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
# 1 ~ N 

buildings =[list(map(int,input().split())) for _ in range(N)]


building =[0]*(N+1)

indegree =[0]*(N+1)

graph =[[]for _ in range(N+1)]

for num in range(len(buildings)):
    for i in range(1,len(buildings[num])):
        if buildings[num][i] == -1: continue
        graph[buildings[num][i]].append(num+1)
        indegree[num+1] += 1


q = deque()
temp =[0]*(N+1)
for i in range(1,N+1):
    building[i] = buildings[i-1][0]
    temp[i] = building[i]
    if indegree[i] == 0:
        q.append(i)


while q:
    v= q.popleft()
    for num in graph[v]:
        temp[num] = max(temp[num],temp[v]+building[num])
        indegree[num] -= 1
        if indegree[num] == 0:
            q.append(num)

for i in range(1,N+1):
    print(temp[i])
