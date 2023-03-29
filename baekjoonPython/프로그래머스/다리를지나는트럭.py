def solution(bridge_length, weight, truck_weights):
    
    answer = 0
    bridge = [0 for _ in range(bridge_length)]
    k = sum(bridge)
    while bridge:
        
        answer += 1
        check = bridge.pop(0)
        if check !=0 :
            k = sum(bridge)
        
        if truck_weights:
            if k + truck_weights[0] <= weight:            
                t = truck_weights.pop(0)
                bridge.append(t)
                k = sum(bridge)
            else:
                bridge.append(0)
                    
    return answer