import sys
def solution(begin, target, words):
    global answer
    answer = sys.maxsize
    
    isUsed = [0]*len(words)
    def dfs(depth,v):
        global answer
        if v == target:
            answer = min(answer,depth)
            return
        
        for i in range(len(words)):
            if not isUsed[i]:
                cnt = 0
                for j in range(len(words[i])):
                    if words[i][j] != v[j]:
                        cnt +=1
                if cnt == 1:
                    isUsed[i] = 1
                    dfs(depth+1,words[i])
                    isUsed[i] = 0
                
    dfs(0,begin)
    
    
    return answer if answer !=sys.maxsize else 0

solution('hit','cog',["hot", "dot", "dog", "lot", "log", "cog"])