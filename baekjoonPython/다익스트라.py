import sys
import heapq

input = sys.stdin.readline

# 도시 개수 N, 버스개수 M
N = int(input())
M = int(input())
distance =[sys.maxsize]*(N+1)
graph =[[]for _ in range(N+1)]

# a 출발 도시 번호, b 도착 도시 번호, c 버스 비용
for _ in range(M):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

# x 출발지, y 목적지
x,y = map(int,input().split())

def dijkstra():
    q = []
    heapq.heappush(q,(x,0))
    
    while q:
        cur,val = heapq.heappop()
        
        if distance[cur] < val : continue
        
        for next,cost in graph[cur]:
            if val+cost < distance[next]:
                distance[next] = val+cost
                heapq.heappush(q,(next,distance[next]))
            
dijkstra()
    
print(distance[y])
