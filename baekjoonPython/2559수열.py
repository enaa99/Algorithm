import sys

input = sys.stdin.readline

N,K = map(int,input().split())

graph = list(map(int,input().split()))


sum_graph = sum(graph[:K])
max_num = sum_graph
for i in range(len(graph)-K):
    sum_graph = sum_graph - graph[i] + graph[i+K]
    max_num = max(max_num,sum_graph)
    
print(max_num)