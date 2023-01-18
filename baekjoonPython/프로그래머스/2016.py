def solution(a, b):
    answer = b-1
    days = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    
    years =[1,3,5,7,8,10,12]
    
    for i in range(2,a):
        if i == 2:
            answer += 29
        elif i in years:
            answer += 31
        else:
            answer += 30
    
    answer %= 7
    
    
    
    return days[answer]

solution(1,1)