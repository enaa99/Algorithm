import sys

input = sys.stdin.readline

graph = list(map(int,input().split()))

answer = 0
for i in graph:
    if i ==0 : continue
    answer += i**2


print(answer%10)