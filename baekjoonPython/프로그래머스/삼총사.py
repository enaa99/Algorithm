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


def solution2(number):
    answer = 0
    
    def DFS(depth,v,cnt):
        nonlocal answer
        if depth == 3:
            if v == 0:
                answer +=1
            return
        
        for i in range(cnt,len(number)):
            DFS(depth+1,v+number[i],i+1)
    
    DFS(0,0,0)
    
    return answer



solution([-2,3,0,2,-5])