def solution(ingredient):
    answer = 0
    
    # 빵, 야채, 고기
    # 1,   2,   3
    cmp = [1,3,2,1]
    burger = []
    for recipe in ingredient:
        burger.append(recipe)
        
        if len(burger) > 3 and recipe == 1:
            tmp = []
            for _ in range(4):
                tmp.append(burger.pop())
            if cmp == tmp:
                answer += 1
            else:
                while tmp:
                    burger.append(tmp.pop())
    
    
    return answer

solution([1,3,2,1,2,1,3,1,2])