def solution(cacheSize, cities):
    answer = 0
    
    arr =[[0,'']for _ in range(cacheSize)]
    
    # 대소문자 구분 X
    
    for city in cities:
        flag = 0
        for cnt in range(len(arr)):
            if arr[cnt][1] == '':
                arr[cnt][1] = city
                answer += 5
                flag = 1
                break
            elif arr[cnt][1].lower() == city.lower():
                answer +=1
                arr[cnt][0] += 1
                flag = 1
                break
        if not flag:
            if arr:
                arr.sort()
                arr[0][0] = 0
                arr[0][1] = city
            else:
                answer += 5
    
    return answer

solution(2,["Jeju", "Pangyo", "NewYork", "newyork"])