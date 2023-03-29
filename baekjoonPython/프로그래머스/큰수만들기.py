def solution(number,k):
    global answer
    answer = 0
    
    len_number = len(number)
    
    def dfs(depth,v,cnt):
        global answer
        if depth == len_number-k:
            answer = max(answer,int(v))
            return
        
        
        for i in range(cnt,len_number):
            if answer and v:
                if int(str(answer)[0]) > int(v[0]):
                    return
            
            dfs(depth+1,v+number[i],i+1)
            
    
    dfs(0,'',0)
        
    
    return str(answer)

solution('1231234',3)