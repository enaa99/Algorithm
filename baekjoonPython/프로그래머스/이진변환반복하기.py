def solution(s):
    cnt = 0
    
    def to_bin(k):
        tmp = 0
        temp =''
        for i in k:
            if i == '0':
                tmp += 1
                continue
            else:
                temp += i
        return [tmp,temp]
    
    check = 0
    while True:
        tmp,s = to_bin(s)
        k = len(s)
        s = format(k,'b')
        
        
        cnt += tmp
        check +=1 
        if s == '1':
            break
    
    
    
    
    return [check,cnt]


solution('110010101001')