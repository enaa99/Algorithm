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
        elif sum_a < sum_b:
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
    
    
    

def solution2(queue1, queue2):
    answer = 0
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    a = sum(queue1)
    b = sum(queue2)
    
    check = len(queue1)*4
    tmp = 0
    
    while True:
        if a > b:
            k = queue1.popleft()
            queue2.append(k)
            a -= k
            b += k
            answer +=1
        elif a < b:
            k = queue2.popleft()
            queue2.append(k)
            a += k
            b -= k
            answer +=1
        else:
            break
        
        tmp +=1
        if tmp == check:
            return -1
    
    
    return answer