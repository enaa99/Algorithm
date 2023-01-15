def solution(food):
    answer = ''
    
    for i in range(1,len(food)):
        if food[i] == 1: continue
        
        k = food[i]//2
        answer += f'{i}'*k
    
    tmp = list(answer)
    answer +='0'
    tmp.reverse()
    for i in tmp:
        answer += i
    
    return answer


solution([1,3,4,6])