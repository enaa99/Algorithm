import sys
from collections import deque

input = sys.stdin.readline


def bfs(start):
    global result
    q = deque()
    q.append(start)
    arr[start] = 0
    while q:
        v = q.popleft()
        if v == K:
            result += 1
            continue
        for i in (v*2, v+1, v-1):
            if 0 <= i < 100001 and (arr[i] == arr[v] + 1 or arr[i] == -1):
                arr[i] = arr[v] + 1
                q.append(i)


N, K = map(int, input().split())
arr = [-1] * 100001
result = 0

bfs(N)

print(arr[K])
print(result)