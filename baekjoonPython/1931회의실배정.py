import sys
import heapq

input = sys.stdin.readline

N = int(input())

l = []
for _ in range(N):
    a,b = map(int,input().split())
    heapq.heappush(l,(b,a))
cnt = check = 0
while l:
    e,s = heapq.heappop(l)
    if check <= s:
        cnt +=1
        check = e
print(cnt)