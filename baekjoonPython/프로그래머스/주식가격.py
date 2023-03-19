def solution(prices):
    
    #모든 prices의 값이 떨어지지 않았다는 가정하에 answer의 값을 초기화한다.
    answer =[i for i in range(len(prices)-1,-1,-1)]
    
    s = [0]
    
    for i in range(1,len(prices)):
        while s and prices[s[-1]] > prices[i]:
            k = s.pop()
            answer[k] = i - k
        s.append(i)
        
    
    return answer

solution([1,2,0,2,3])
