import heapq

class Solution:
    def mostBooked(n: int, meetings:list) -> int:
        meetings.sort()
        free_rooms = [i for i in range(n)]
        busy_rooms = []
        count = [0] * n
        
        for start, end in meetings:
            while busy_rooms and busy_rooms[0][0] <= start:
                _, room = heapq.heappop(busy_rooms)
                heapq.heappush(free_rooms, room)
            
            if free_rooms:
                room = heapq.heappop(free_rooms)
            else:
                end_time, room = heapq.heappop(busy_rooms)
                end += end_time - start
            
            heapq.heappush(busy_rooms, (end, room))
            count[room] += 1
        
        cnt = max(count)
        for i in range(n):
            if count[i] == cnt:
                return i