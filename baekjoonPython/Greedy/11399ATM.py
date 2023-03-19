import sys

input = sys.stdin.readline

N = int(input())

graph = list(map(int,input().split()))

graph.sort()

answer = 0

for i in range(len(graph)):
    answer += graph[i]
    graph[i] = answer
    

print(sum(graph))