
from collections import deque
def solution(scores):
    answer = 1
    
    # 근무 태도 점수 & 동료 평가 점수
    # 다른 임의의 사원보다 두 점수가 모두 낮은 경우 한번이라도 있다면 인센 X
    # 합에 따른 석차에 따라 인센
    # 동석차 존재
    # scores[0] 완호 점수
    # 인센 없을 때, -1
    x,y = scores[0][0], scores[0][1]
    u = x+y
    scores.sort(key = lambda x:(-x[0],x[1]))
    
    k = 0
    for a,b in scores:
        
        if a >x and b>y:
            return -1
        
        if k <= b :
            k = b
            if u < a+b:
                answer +=1
        
    

    
    return answer

