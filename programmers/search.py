from collections import deque

def solution(office, k):
    answer = -1
    move = [[0,1], [1,0]]
    
    
    def heater(x,y,length):
        q = deque()
        n,m = 0, len(office)

        isVisited = [[0]*m for i in range(m)]
        
        check = 0
        q.append([x,y])
        if office[x][y] == 1:
            check +=1
        
        
        while q:
            a,b = q.popleft()
            for o,p in move:
                xa = o+a
                ya = p +b

                if xa <n or ya<n or xa>=m or ya>=m or isVisited[xa][ya]: continue
                if xa>=x+length or ya>=y+length: continue
                
                if office[xa][ya] == 1:
                    check+=1
                
                isVisited[xa][ya] =1
                q.append([xa,ya])
                
        return check
    len_office = len(office)
    
    for i in range(len_office):
        for j in range(len_office):
            if i+k> len_office or j+k >len_office: continue
            
            answer = max(answer,heater(i,j,k))
            
    return answer


solution([[1,0,0,0],[0,0,0,1],[0,0,1,0],[0,1,1,0]],2)