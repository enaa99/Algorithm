import sys
import heapq
input = sys.stdin.readline

n = int(input())
l = []
for _ in range(n):
    k = int(input())
    heapq.heappush(l,k)

answer = 0

if len(l) == 1: 
    print(0)
    exit(0)

while True: 
    a = heapq.heappop(l) 
    b = heapq.heappop(l) 
    answer += a + b 
    heapq.heappush(l, a + b)
    if len(l) <= 1:break
        
print(answer)