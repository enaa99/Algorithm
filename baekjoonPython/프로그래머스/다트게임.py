def solution(dartResult):    
    dart = []
    # 자를 때, 숫자인지 점수 0~10점까지
    if '10' in dartResult:
        dartResult = dartResult.replace('10','A')
    
    numbers =['0','1','2','3','4','5','6','7','8','9','A']
    point =[]
    for i in range(len(dartResult)):
        if dartResult[i] in numbers:
            if dartResult[i] == 'A':
                point.append(10)
            else:
                point.append(int(dartResult[i]))
        else:
            if dartResult[i] == 'S': continue
            elif dartResult[i] == 'D':
                point[-1] **= 2
            elif dartResult[i] == 'T':
                point[-1] **= 3
            elif dartResult[i] == '*':
                if len(point) > 1:
                    point[-2] *= 2
                point[-1] *= 2
            else:
                point[-1] = -point[-1]
    
    return sum(point)


solution('1S*2T*3S')