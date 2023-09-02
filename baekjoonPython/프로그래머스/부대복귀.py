from collections import deque
import heapq
def solution(n, roads, sources, destination):
    answer = []
    
    road = [[] for _ in range(n+1)]
    
    for a,b in roads:
        road[a].append(b)
        road[b].append(a)
    
    isVisited = [-1]*(n+1)
    def dijkstra(start):
        q = []
        
        
        isVisited[start] = 0
        heapq.heappush(q,[0,start])
            
        while q:
            value, dest = heapq.heappop(q)
                
            for i in road[dest]:
                if isVisited[i] == -1:
                    isVisited[i] = value + 1
                    
                    heapq.heappush(q,[value+1,i])
                    
    
    dijkstra(destination)

    
    return [isVisited[i] for i in sources]

solution(3,	[[1, 2], [2, 3]],[2,3],1)