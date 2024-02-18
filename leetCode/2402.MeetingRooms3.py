import heapq

class Solution:
    def mostBooked(n: int, meetings:list) -> int:
        meetings.sort()
        free = [i for i in range(n)]
        busy = []
        count = [0] * n
        
        for start, end in meetings:
            while busy and busy[0][0] <= start:
                _, room = heapq.heappop(busy)
                heapq.heappush(free, room)
            
            if free:
                room = heapq.heappop(free)
            else:
                end_time, room = heapq.heappop(busy)
                end += end_time - start
            
            heapq.heappush(busy, (end, room))
            count[room] += 1
        
        cnt = max(count)
        for i in range(n):
            if count[i] == cnt:
                return i
