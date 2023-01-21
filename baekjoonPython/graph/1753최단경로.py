import sys
import heapq

input = sys.stdin.readline

V,E = map(int,input().split())

start = int(input())

graph = [[]for _ in range(V+1)]

for _ in range(E):
    u,v,w = map(int,input().split())
    graph[u].append([w,v])
    
    
distance =[sys.maxsize]*(V+1)

def dijkstra(start):
    q = []
    q.append([0,start])
    distance[start] = 0
    
    while q:
        dist,pos = heapq.heappop(q)
        
        if distance[pos] < dist: continue
        
        for d,n in graph[pos]:
            next_dist = distance[pos] + d
            if distance[n] > next_dist:
                distance[n] = next_dist
                heapq.heappush(q,[next_dist,n])

dijkstra(start)

for i in range(1,len(distance)):
    if distance[i] == sys.maxsize:
        print('INF')
    else:
        print(distance[i])