def solution(word):
    global answer
    answer = 0
    
    words = ['A','E','I','O','U']
    len_w = len(word)
    
    def dfs(cnt):
        global answer
        if cnt == word:
            return True
        
        elif len(cnt) == 5: return False
        
        for i in words:
            answer += 1
            if dfs(cnt+i):
                return True
    
    dfs('')
    
    
    return answer