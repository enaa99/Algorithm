import sys

input = sys.stdin.readline

N = int(input())


graph = [[0]*100 for _ in range(100)]

answer = 0
for _ in range(N):
    a,b = map(int,input().split())
    
    for i in range(a,a+10):
        for j in range(b,b+10):
            if not graph[i][j]:
                graph[i][j] = 1
                answer +=1

print(answer)
