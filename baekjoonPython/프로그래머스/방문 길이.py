from collections import defaultdict
def solution(dirs):
    answer = 0
    
    dict ={'U':[1,0],'L':[0,1],'R':[0,-1],'D':[-1,0]}
    isVisited = defaultdict(list)
    
    
    x = y = 0
    for direc in dirs:
        a,b = dict[direc]
        xa = x + a
        ya = y + b
        
        if xa > 5 or ya > 5 or xa <-5 or ya <-5: continue
        
        if [x,y] not in isVisited[xa,ya]:
            isVisited[xa,ya].append([x,y])
            isVisited[x,y].append([xa,ya])
            answer +=1
        
        
        x,y = xa,ya
    
    
    return answer


solution("ULURRDLLU")