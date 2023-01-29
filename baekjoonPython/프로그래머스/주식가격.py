def solution(prices):
    
    # 최대값잡아주기
    answer =[i for i in range(len(prices)-1,-1,-1)]
    
    s = [0]
    
    for i in range(1,len(prices)):
        while s and prices[s[-1]] > prices[i]:
            k = s.pop()
            answer[k] = i - k
        s.append(i)
        
    
    return answer

solution([4,1,2,3,4,5,1,6,3,1,2,1])
