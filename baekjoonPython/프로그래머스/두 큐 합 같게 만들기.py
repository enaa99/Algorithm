from collections import deque
def solution(queue1, queue2):
    
    sum_a = sum(queue1)
    sum_b = sum(queue2)
    
    
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    tmp = len(queue1)*4
    
    
    cnt = 0
    flag = 0
    while True:
        if sum_a > sum_b:
            k= queue1.popleft()
            queue2.append(k)
            sum_a -= k
            sum_b += k
        elif sum(queue1) < sum(queue2):
            k = queue2.popleft()
            queue1.append(k)
            sum_a += k
            sum_b -= k
        else:
            break
        
        cnt += 1
        
        if cnt == tmp:
            return -1
    
    return cnt
    
    
    
    