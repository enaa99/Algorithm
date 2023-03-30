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




# def solution(number, k):
#     s = [number[0]]
    
#     for num in number[1:]:
#         while s and s[-1] < num and k>0:
#             s.pop()
#             k -= 1
#         s.append(num)
#     if k!=0:
#         s = s[:len(s)-k]
    
#     return ''.join(s)

