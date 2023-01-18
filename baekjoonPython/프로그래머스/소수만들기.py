def solution(nums):
    answer = []
    
    
    def isPrime(k):
        for i in range(2,int(k**0.5)+1):
            if k%i == 0:
                return False
        return True
    
    
    arr = [0]*3
    def dfs(depth,v):
        if depth == 3:
            k = sum(arr)
            if isPrime(k):
                answer.append(k)
            return
        for i in range(v,len(nums)):
            arr[depth] = nums[i]
            dfs(depth+1,i+1)
    
    dfs(0,0)
    return len(answer)