def solution(diffs, times, limit):
    answer = 0
    
    
    # diff <= level => + time_cur
    # diff > level => (diff - level) * (time_cur + time_prev) + time_cur
    
    # level select
    
    def check(mid):
        count = 0
        for i in range(len(diffs)):
            prev = times[i-1] if i > 0 else 0
            if diffs[i] > mid:
                count += (diffs[i] - mid) * (times[i] + prev) + times[i] 
            else:
                count += times[i]
        return count <= limit
            
    
    l = 0
    r = max(diffs) + 1
    
    while l+1 < r:
        mid = (l+r)//2
        if check(mid):
            r = mid
        else:
            l = mid
    
    return r