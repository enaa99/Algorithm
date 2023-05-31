from collections import deque
def solution(order):
    answer = 0
    
    s = []
    order = deque(order)


    for i in range(len(order)):
        if i+1 != order[0]:
            s.append(i+1)
        else:
            order.popleft()
            answer +=1
            while s:
                if s[-1] == order[0]:
                    s.pop()
                    order.popleft()
                    
                    answer +=1
                else:
                    break
        
        
    return answer

solution([4, 3, 1, 2, 5])


def solution2(order):
    answer = 0
    s = []
    cnt = 0
    
    for i in range(1,len(order)+1):
        s.append(i)
        
        while s and s[-1] == order[cnt]:
            s.pop()
            answer +=1
            cnt +=1
    
    
    
    return answer