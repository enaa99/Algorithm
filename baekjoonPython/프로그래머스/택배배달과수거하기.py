def solution(cap, n, deliveries, pickups):
    answer = 0
    # cap 최대 택배 상자 적재
    # n 집 개수
    # 거꾸로

    deliver, pickup = 0,0
    
    for i in range(n-1,-1,-1):
        deliver += deliveries[i]
        pickup += pickups[i]
    
        while deliver > 0 or pickup > 0:
            deliver -= cap
            pickup -= cap
            
            answer += (i+1)*2
    
    
    return answer