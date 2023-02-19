def solution(numbers,target):
    global answer
    answer = 0
    
    k = numbers[0]*2
    def DFS(v,depth,cnt):
        global answer
        
        if depth == len(numbers)-1 :
            if v == target or v-k == target:
                answer +=1 
                return
        
        for i in range(cnt+1,len(numbers)):
            DFS(v+numbers[i],depth+1,i)
            DFS(v-numbers[i],depth+1,i)
        
    DFS(numbers[0],0,0)
    
    return answer
solution([1,1,1,1,1],3)