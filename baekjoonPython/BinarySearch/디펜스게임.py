def solution(n, k, enemy):
    
    def check(arr):
        arr.sort(key = lambda x:-x)
        
        arr = arr[k:]
        if sum(arr) > n:
            return False
        return True
    
    l = 0
    r = len(enemy)
    
    while l+1 < r:
        mid = (l+r)//2
        arr = enemy[:mid]
        
        if check(arr):
            l = mid
        else:
            r = mid
    
    
    return l