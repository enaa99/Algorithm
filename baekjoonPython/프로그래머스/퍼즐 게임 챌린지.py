def solution(diffs, times, limit):
    answer = 0
    
    # 현재 퍼즐의 난이도 diff
    # 현재 퍼즐의 소요시간 time_cur
    # 이전 퍼즐의 소요시간 time_prev
    # 숙련도 level
    
    # diff <= level -> time_cur 시간 소요
    # diff > level -> diff - level 번 틀림, 틀릴 때마다 time_cur 시간 사용, 
    # 추가로 time_prev 만큼 시간 사용
    # 이전 퍼즐을 풀때에는 틀리지 않음, diff-level번 틀린 이후, time_cur 만큼의 시간 사용하여 퍼즐 해결
    # 숙련도의 최소값
    # binart_search
    
    def check(level):
        time = 0
        for i in range(len(diffs)):
            prev = times[i-1] if i > 0 else 0
            if diffs[i] <= level:
                time += times[i]
            else:
                count = diffs[i] - level
                time += count*(times[i]+prev) + times[i]
        
        return time <= limit
                        
    
    l = 0
    r = max(diffs) + 1
    
    while l + 1 < r:
        mid = (l+r)//2
        
        if check(mid):
            r = mid
        else:
            l = mid
    
    return r