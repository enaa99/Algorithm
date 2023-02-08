import sys

input = sys.stdin.readline

N = int(input())


graph = [int(input()) for _ in range(N)]

graph.sort()
answer =0
length = len(graph)
for i in range(length):
    answer = max(graph[i]*(length-i),answer)
    
print(answer)