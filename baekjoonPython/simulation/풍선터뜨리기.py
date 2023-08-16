def solution(a):
    answer = 1
    
    min_a = min(a)
    
    pos = a.index(min_a)
    
    l = 0
    r = len(a)-1
    
    min_l = a[l]
    min_r = a[r]
    
    
    while l<pos or r>pos:
        l+=1
        r-=1
        
        if l <= pos and a[l] < min_l:
            answer +=1
            print(min_l)
            min_l = a[l]
        
        if r >= pos and a[r] < min_r:
            answer +=1
            print(min_r)
            
            min_r = a[r]
        
        
    
    
    return answer

solution([27,65,-16,-2,58] )