import sys
from collections import deque
import heapq

input = sys.stdin.readline



jobs = [[1, 8], [0, 20], [2, 6]]

def solution(jobs):
    answer = 0
    l = list(set())
    jobs.sort(key=lambda x:x[0])
    
    
    check =min(jobs)
    print(check)
    low,high = jobs[0][0], jobs[0][1]
    tmp = high - low
    jobs.sort(key=lambda x:x[1]-x[0])
    print(jobs)

    
    while l:
        start, end = heapq.heappop(l)
        
        if high < -start: 
            heapq.heappush(l,(start,end))
            continue
        tmp += end + start
        high = end
    answer = tmp//len(jobs) 
    return answer

print(solution(jobs))