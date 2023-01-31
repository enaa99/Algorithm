def solution(n,k):
    answer = 0
    
    # 소수는 0 포함 X
    def isPrime(k):
        
        for j in range(2,int(k**0.5)+1):
            if k%j ==0:
                return False
        return True
    
    
    
    def change(n,k):
        
        base =''
        while n> 0:
            n,mod =divmod(n,k)
            base += str(mod)
        return base[::-1]
        
    num = change(n,k)
    
    
    
    num_graph = num.split('0')
    
    for i in num_graph:
        if not i: continue
        if isPrime(int(i)) and int(i) > 1:
            answer +=1
    
    return answer


solution(110011,10)