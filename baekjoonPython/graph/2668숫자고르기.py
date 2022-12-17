import sys
from collections import deque

input = sys.stdin.readline

N = int(input())


l = [0 for _ in range(N+1)]

for i in range(1,N+1):
    l[i] = int(input())

answer = set()

def DFS(value,low,high):
    low.add(value)
    high.add(l[value])
    if l[value] in low:
        if low == high:
            answer.update(low)
            return True
        return False
    return DFS(l[value],low,high)

for i in range(1,N+1):
    if i not in answer:
        DFS(i,set(),set())
    

print(len(answer))
print(*sorted(answer),sep="\n")



