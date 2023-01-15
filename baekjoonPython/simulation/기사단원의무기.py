def solution(number, limit, power):
    answer = 0
    
    def check(k,cnt):
        for i in range(1,int(k**0.5)+1):
            if k%i == 0:
                if i == k//i: # 제곱근
                    cnt +=1
                else: # 제곱근이 아닐경우 ex) 2x3
                    cnt +=2
        if cnt > limit:
            return power
        return cnt

    for i in range(1,number+1):
        answer += check(i,0)
    
    return answer

solution(5,3,2)