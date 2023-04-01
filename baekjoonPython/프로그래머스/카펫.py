def solution(brown, yellow):
    # 가로 >= 세로 , a>=b
    
    check = brown + yellow
    
    k = check//2 + 2 - yellow//2
        
    a = b = k//2
    
    if a+b != k:
        a+=1
    
    while a*b != check :
        a +=1
        b -=1
    answer = [a,b]
    
    return answer