def solution(storey):
    answer = 0
    # 0 층으로 가기
    # 1억 그리디?
    # 항상 10기준 가까운 곳으로 가기
    
    store = str(storey)
    tmp = []
    for i in range(len(store)-1,-1,-1):
        tmp.append(int(store[i]))
    
    cnt = 0
    for num in range(len(tmp)):
        if 5 >= tmp[num]:
            cnt += tmp[num]
            
            tmp[num] = 0
            
        else:
            cnt += 10 - tmp[num]
            if num != len(tmp)-1:
                tmp[num+1] +=1
            tmp[num] = 0            
    
    
    return tmp

solution(16)