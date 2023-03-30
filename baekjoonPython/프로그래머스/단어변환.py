import sys
from collections import deque
def solution(begin, target, words):
    global answer
    answer = sys.maxsize
    
    # isUsed = [0]*len(words)
    # def dfs(depth,v):
    #     global answer
    #     if v == target:
    #         answer = min(answer,depth)
    #         return
    
    #     for i in range(len(words)):
    #         if not isUsed[i]:
    #             cnt = 0
    #             for j in range(len(words[i])):
    #                 if words[i][j] != v[j]:
    #                     cnt +=1
    #             if cnt == 1:
    #                 isUsed[i] = 1
    #                 dfs(depth+1,words[i])
    #                 isUsed[i] = 0
    
    # dfs(0,begin)
    
    def bfs():
        q = deque()
        q.append([begin,[],0])
        while q:
            v,k,tmp = q.popleft()
            
            if v == target:
                return tmp
            
            for num in words:
                cnt = 0
                for i in range(len(num)):
                    if num in k: break
                    
                    if num[i] != v[i]:
                        cnt +=1
                if cnt == 1:
                    check = k[:]
                    check.append(num)
                    q.append([num,check,tmp+1])
        return 0
    
    
    return bfs()

solution('hit','cog',["hot", "dot", "dog", "lot", "log", "cog"])