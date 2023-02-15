import heapq
import datetime


def solution(book_time):
    answer = 0
    
    heapq.heapify(book_time)
    use =[]
    while book_time:
        start,end =heapq.heappop(book_time)
        hour,minute = end.split(':') 
        e_time =datetime.timedelta(hours=int(hour),minutes=int(minute)+10)
        if not use:
            answer +=1
            heapq.heappush(use,e_time)
            
        else:
            v = heapq.heappop(use)
            s_hour,s_minute = start.split(':')
            
            s_time = datetime.timedelta(hours=int(s_hour),minutes=int(s_minute))
            if v <= s_time:
                heapq.heappush(use,e_time)
            else:
                heapq.heappush(use,v)
                heapq.heappush(use,e_time)
                answer +=1
    
    
    return answer

solution([["09:10", "10:10"], ["10:20", "12:20"]])