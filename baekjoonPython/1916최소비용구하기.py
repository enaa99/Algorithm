import sys
import heapq

input = sys.stdin.readline

# 도시 개수 N, 버스개수 M
N = int(input())
M = int(input())
distance =[sys.maxsize]*(N+1)
l =[[]for _ in range(N+1)]
# a 출발 도시 번호, b 도착 도시 번호, c 버스 비용
for _ in range(M):
    a,b,c = map(int,input().split())
    l[a].append((b,c))

# x 출발지, y 목적지
x,y = map(int,input().split())
temp = []
def dijkstra(start):
    heapq.heappush(temp,start)
    distance[start[0]] = 0
    while temp:
        current, dist = heapq.heappop(temp)
        if distance[current] < dist : continue
        
        for i in l[current]:
            next, nextdist = i[0],dist + i[1]
            if distance[next] > nextdist:
                distance[next] = nextdist
                heapq.heappush(temp,(next,nextdist))
        
dijkstra((x,0))

print(distance[y])