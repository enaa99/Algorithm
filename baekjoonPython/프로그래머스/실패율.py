def solution(N,stages):
    answer =[]
    
    # 전체 스테이지 개수 N
    # 현재 멈춰있는 스테이지 번호 stages
    # 내림차순
    # 실패율 = 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
    
    
    stages.sort()
    
    stage = [0]*(N+2)
    people = len(stages)
    
    for i in stages:
        stage[i] += 1
    
    for i in range(1,len(stage)):
        if people == 0: break

        answer.append([stage[i]/people,i])
        people -= stage[i]
    
    if len(answer) < N:
        while len(answer) < N: answer.append([0,len(answer)+1])
    
    answer.sort(key=lambda x:(-x[0],x[1]))
    
    ans = []
    for i,j in answer:
        if j > N: continue
        ans.append(j)
    
    return ans


solution(5,[2,1,2,6,2,4,3,3])