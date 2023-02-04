N = int(input())

graph = [list(map(int,input().split())) for _ in range(N)]


graph.sort(key=lambda x:(x[1],x[0]))



for i,j in graph:
    print(i,j)