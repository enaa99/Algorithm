import sys
import heapq

input = sys.stdin.readline

N = int(input())

cards = [int(input()) for _ in range(N)]

heapq.heapify(cards)

if N == 1:
    print(0)
    exit(0)
answer =0 
while len(cards)>=2:
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    
    heapq.heappush(cards,a+b)
    answer += a+b

print(answer)