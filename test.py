import sys

input = sys.stdin.readline

N,K = map(int,input().split())

graph = list(map(int,input().split()))

graph.sort(reverse=True)

print(graph[K-1])