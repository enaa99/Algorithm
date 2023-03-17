def solution(babbling):
    answer =0
    
    baby = [ "aya", "ye", "woo", "ma" ]
    
    
    for num in babbling:
        bab = ''
        for i in num:
            bab += i 
            
            if bab in baby:
                bab = ''
        if not bab:
            answer +=1
    
    return answer


solution(["aya", "yee", "u", "maa", "wyeoo"])