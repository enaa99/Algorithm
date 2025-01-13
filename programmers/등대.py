def solution(n, lighthouse):
    answer = 0
    
    # 등대가 반드시 한개는 켜져 있어야 한다.
    # 연결되어 있는 등대를 찾는다 
    lists = [[] for _ in range(n+1)]
    light = [[i,0] for i in range(n+1)]
    light_check = [0] * (n+1)
    
    for a,b in lighthouse:
        lists[a].append(b)
        lists[b].append(a)
        light[a][1] += 1
        light[b][1] += 1
    
    light.sort(key=lambda x:-x[1])
    
    
    check = 0
    for idx, count in light:
        answer += 1
        check +=1
        for i in lists[idx]:
            light_check[i] += 1
        
        for i in light_check:
            if i != 0:
                check +=1
        
        if check >= n:
            break
        
    
    
    return answer


solution(8, [[1, 2], [1, 3], [1, 4], [1, 5], [5, 6], [5, 7], [5, 8]])