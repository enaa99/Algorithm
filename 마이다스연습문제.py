import sys
def solution(n, m, x, y, z):
    answer = []
    # 시작 도시와 끝 도시의 모든 N^2 가지 쌍의 사전 순 최단 경로에 포함된 횟수를 나타낸다
    INF = sys.maxsize
    graph = [[INF]*(n+1) for _ in range(n+1)]

    # 교통량
    dist = [[i,0] for i in range(1,n+1)]

    for i in range(1, n+1):
        graph[i][i] = INF
    
    for i in range(m):
        graph[x[i]][y[i]] = z[i]
        graph[y[i]][x[i]] = z[i]
    
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if i==j: continue
                if graph[i][j] > graph[i][k]+graph[k][j]:
                    graph[i][j] = graph[i][k]+graph[k][j]
                    dist[k-1][1] += 1
                
    dist.sort(key=lambda x:(-x[1],x[0]))    
                
    return dist


solution(3,3,[1,1,2],[3,2,3],[1,5,2])