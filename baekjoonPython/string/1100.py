import sys

input = sys.stdin.readline


graph = [list(input().rstrip()) for _ in range(8)]
answer = 0
for num in range(len(graph)):
    for i in range(len(graph[num])):
        if num%2 == 0:
            if i%2 == 0 and graph[num][i] == 'F':
                answer +=1
        else:
            if i%2==1 and graph[num][i] == 'F':
                answer +=1
print(answer)