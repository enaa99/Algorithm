def solution(targets):
    answer = 1
    
    targets.sort(key=lambda x:(x[1],x[0]))
        
        
    point = targets[0][1]
    
    for start,end in targets:
        if point <= start:
            answer +=1
            point = end
            
        
    
    
    
    return answer





solution([[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]])