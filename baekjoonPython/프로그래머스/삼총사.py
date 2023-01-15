def solution(number):
    answer = 0
    
    
    arr =[0]*3
    check = []
    isUsed =[0]*len(number)
    
    def dfs(cnt,v):
        if cnt == 3:
            check.append(arr[:])
            return

        for i in range(v,len(number)):
            if not isUsed[i]:
                isUsed[i] = True 
                arr[cnt] = number[i]
                dfs(cnt+1,i+1)
                isUsed[i] = False
    
    dfs(0,0)
    
    for a,b,c in check:
        if a+b+c == 0:
            answer +=1
    
                
    return answer




solution([-2,3,0,2,-5])