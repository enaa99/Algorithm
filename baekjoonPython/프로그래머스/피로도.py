def solution(k,dungeons):
    global answer
    answer =0
    
    # 던전의 각 행
    # ["최소필요피로도", "소모피로도"]
    # 소모할 수 있는 최대 던전 수
    # 현재 피로도 k
    # DFS?
    isVisited =[0]*len(dungeons)
    len_d = len(dungeons)
    def DFS(v,cnt):
        global answer
        answer = max(cnt,answer)
        if cnt >= len_d:
            return
        
        for i in range(len(dungeons)):
            if dungeons[i][0] <= v and not isVisited[i]:
                isVisited[i] = 1
                DFS(v-dungeons[i][1],cnt+1)
                isVisited[i] = 0
    
    DFS(k,0)
    
    return answer

solution(80,[[80,20],[50,40],[30,10]])