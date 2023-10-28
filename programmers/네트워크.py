from collections import deque
def solution(n, computers):
    answer = 0
    
    
    graph = [[] for _ in range(n)]
    
    for i in range(n):
        for j in range(len(computers[i])):
            if i == j: continue
            
            if computers[i][j] == 1:
                if j not in graph[i] and i not in graph[j]:
                    graph[i].append(j)
                    graph[j].append(i)
    
    
    isVisited = [0 for _ in range(n)]
    
    
    def check(start):
        q = deque()
        isVisited[start] = 1
        
        q.append(start)
        
        while q:
            v = q.popleft()
            
            for i in graph[v]:
                if not isVisited[i]:
                    isVisited[i] = 1
                    q.append(i)
    
    
    
    for i in range(n):
        if not isVisited[i]:
            check(i)
            answer +=1
    
    
    
    return answer
solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]])