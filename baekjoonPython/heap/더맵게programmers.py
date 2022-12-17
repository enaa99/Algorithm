import sys
import heapq

input = sys.stdin.readline

a = list(map(int,input().split()))
b = int(input())


def solution(scoville, K):
    answer = 0
    l = []
    for i in scoville:
        heapq.heappush(l,i)
    
    while l:
        v = heapq.heappop(l)
        if v < K:
            if l:
                v2 = heapq.heappop(l)
                tmp = v +(v2*2)
                answer +=1
                heapq.heappush(l,tmp)
            else:
                return -1
        else:
            return answer
    
solution(a,b)