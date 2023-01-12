def solution(t, p):
    answer = 0
    t = list(t)
    cmp = len(p)-1
    
    for i in range(cmp,len(t)):
        tmp = ""
        for j in range(i-cmp,i+1):
            tmp += t[j]
        if int(tmp) <= int(p):
            answer +=1
        
    return answer

solution("500220839878", "7")