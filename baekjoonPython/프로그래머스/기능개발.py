def solution(progresses, speeds):
    answer = []
    
    # 배포할때 몇개의 기능이 한번에 배포가 되는가? check
    cnt = 0
    for i in range(len(progresses)):
        progresses[i] += speeds[i]*cnt
        if progresses[i] >= 100:
            answer[-1] +=1
            continue
        
        while progresses[i] < 100:
            cnt += 1
            progresses[i] += speeds[i]
        
        answer.append(1)
    
    
    
    return answer