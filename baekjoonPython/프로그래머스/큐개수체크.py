from collections import defaultdict
from collections import deque
def solution(q):
    
    answer = 0
    counts = len(q)//3
    q= deque(q)
    
    check = defaultdict(int)
    
    for i in q:
        check[i] +=1
    
    while True:
        if check[1] == check[2] == check[3]:
            break
        
        answer +=1
        check[q.popleft()] -=1
        
        
        for i in check.keys():
            if check[i] < counts:
                check[i] +=1
                q.append(i)
                break
        
    return answer


solution([1,1,1,2,3,3,2,2])

