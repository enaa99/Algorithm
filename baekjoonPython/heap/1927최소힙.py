import sys
import heapq

input = sys.stdin.readline

N = int(input())

q = []

for _ in range(N):
    k = int(input())
    if k != 0:
        heapq.heappush(q,k)
    else:
        if q:
            print(heapq.heappop(q))
        else:
            print(0)
