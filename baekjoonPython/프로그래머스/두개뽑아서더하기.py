def solution(numbers):
    answer = set()
    
    arr = [0]*2
    def dfs(depth,v):
        if depth == 2:
            answer.add(sum(arr))
            return
        
        for i in range(v,len(numbers)):
                arr[depth] = numbers[i]
                dfs(depth+1,i+1)
                
    dfs(0,0)
    
    
    return sorted(list(answer))

