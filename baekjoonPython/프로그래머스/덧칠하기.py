def solution(n,m,section):
    answer = 0
    
    #  n 구역 길이 , m 롤러 길이 , section 칠해야 할 공간 담긴 배열, 
    q = []
    for area in section:
        if not q:
            k = m + area - 1
            q.append(k)
        else:
            if area <= q[-1] : continue
            
            k = m+area -1 
            q.append(k)
    
    
    return len(q)

solution(8,4,[2,3,6])