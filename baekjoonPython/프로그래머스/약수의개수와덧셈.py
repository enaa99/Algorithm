def solution(left, right):
    answer = 0
    
    
    for i in range(left,right+1):
        tmp =0 
        for k in range(2,int(i**0.5)+1):
            if i%k == 0:
                if k == i//k:
                    tmp +=1
                else:
                    tmp +=2
        if tmp%2 == 0 and tmp!=0:
            answer += i
        else:
            answer -= i
                    
    return answer

solution(13,17)