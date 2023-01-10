import sys
import heapq

input = sys.stdin.readline

N, K = map(int, input().split())
jewerly = []
for _ in range(N):
    heapq.heappush(jewerly, list(map(int,input().split())))

bags = [int(input()) for _ in range(K)]

bags.sort()

answer = 0

tmp = []

for bag in bags:
    while jewerly and bag >= jewerly[0][0]:
        w,v = heapq.heappop(jewerly)
        heapq.heappush(tmp, -v)
    if tmp:
        answer -= heapq.heappop(tmp)
    # elif not jewerly:
    #     break
print(answer)