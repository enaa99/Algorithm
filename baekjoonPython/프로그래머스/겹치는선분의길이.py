def solution(lines):
    answer = 0
    
    graph = [0]*201
    
    for start,end in lines:
        i = start+100
        flag = 0
        tmp = 0
        while i < end+100:
            if graph[i] == 1 and not flag:
                flag =1
                tmp = i
                graph[i] = 1
            elif graph[i] == 0 and flag:
                flag = 0
                answer += abs(i-tmp)
                graph[i] = 2
            else:
                graph[i] = 1
            i +=1
                
            
    
    
    return answer

solution([[0, 1], [2, 5], [3, 9]])