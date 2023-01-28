import sys
import heapq

input = sys.stdin.readline

# 절대값이 가장 작은 값, 가장 작은 값이 여러개일 때는, 가장 작은 수를 출력, 그 값을 배열에서 제거

N = int(input())

# 최소힙
array_plus = []
# 최대힙 
array_minus = []

for _ in range(N):
    k = int(input())
    
    if k == 0:
        a = b = sys.maxsize
        if not array_plus and not array_minus:
            print(0)
            continue
        
        if array_plus:
            a = heapq.heappop(array_plus)
        if array_minus:
            b = heapq.heappop(array_minus)
        
        if a < b:
            if b != sys.maxsize:
                heapq.heappush(array_minus,b)
            print(a)
        else:
            if a != sys.maxsize:
                heapq.heappush(array_plus,a)
            print(-b)
        
    
    elif k > 0 :
        heapq.heappush(array_plus,k)
    else:
        heapq.heappush(array_minus,-k)
