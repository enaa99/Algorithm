def solution(order):
    answer = 0
    
    s = []
    len_order = len(order) + 1
    start = 0
    
    for i in range(1, len_order):
        if i == order[start]:
            answer +=1
            start +=1
        else:
            while s and s[-1] == order[start]:
                start +=1
                answer +=1
                s.pop()
            else:
                s.append(i)
    
    while s and s[-1] == order[start]:
        start +=1
        answer +=1
        s.pop()
    
    return answer

solution([5,4,3,2,1])