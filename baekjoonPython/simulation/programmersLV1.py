def solution(a, b):
    answer = ''
    
    days = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    
    
    check = [1,3,5,7,8,10,12]
    cnt = 0
    for i in range(1,a):
        if i in check:
            cnt += 31
        elif i == 2:
            cnt += 29
        else:
            cnt += 30
    
    cnt += b
    
    cnt = cnt%7
    
    
    
    return days[cnt]


solution(5,24)