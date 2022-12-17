import sys
import heapq

input = sys.stdin.readline

heapL = []
heapR = []
ans = []

for _ in range(int(input())):
    k = int(input())
    if len(heapL) == len(heapR):
        heapq.heappush(heapL,(-k,k))
    else:
        heapq.heappush(heapR,k)
        

    if  heapR and heapL[0][1] > heapR[0]:
        a = heapq.heappop(heapR)
        b = heapq.heappop(heapL)[1]
        heapq.heappush(heapL,(-a,a))
        heapq.heappush(heapR,b)
    
        
    ans = heapL[0][1]
    
    print(ans)