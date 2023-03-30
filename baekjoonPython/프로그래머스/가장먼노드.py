from collections import deque
def solution(n, edge):
    answer = 0
    
    graph = [[] for _ in range(n+1)]
    
    for a,b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    isVisited = [0]*(n+1)
    dist = [0]*(n+1)
    
    def bfs():
        q = deque()
        q.append([1,1])
        isVisited[1] = 1
        while q:
            k,cnt = q.popleft()
            
            for node in graph[k]:
                if not isVisited[node]:
                    isVisited[node] = 1
                    dist[node] = cnt +1
                    q.append([node,cnt+1])
    bfs()
    
    k = max(dist)
    
    answer = dist.count(k)
    
    return answer

solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])