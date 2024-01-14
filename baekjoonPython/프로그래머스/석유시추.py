from collections import defaultdict, deque

def solution(land):
    answer = 0
    
    oil_dic = defaultdict(int)
    voil_dic = defaultdict(int)
    isVisited = [[0]*len(land[i]) for i in range(len(land))]
    value = 1
    def BFS(a,b,value):
        dx = [1,0,-1,0]
        dy = [0,1,0,-1]
        q = deque()
        isVisited[a][b] = 1
        q.append([a,b])
        oil_dic[f"{a},{b}"] = value

        count = 1
        while q:
            x,y = q.popleft()
            for i in range(4):
                xa = x + dx[i]
                ya = y + dy[i]
                
                if xa < 0 or ya < 0 or xa>= len(land) or ya>=len(land[0]): continue
                
                if land[xa][ya] ==1 and isVisited[xa][ya] != 1:
                    oil_dic[f"{xa},{ya}"] = value
                    q.append([xa,ya])
                    isVisited[xa][ya] = 1
                    count +=1
        voil_dic[value] = count
        
        
    
    for i in range(len(land[0])):
        sum_oil = 0
        isUsed = defaultdict(int)
        for j in range(len(land)):
            if land[j][i] == 1 and isUsed[oil_dic[f"{j},{i}"]] != 1:
                if isVisited[j][i] == 0:
                    BFS(j,i,value)
                    value +=1
                
                sum_oil += voil_dic[oil_dic[f"{j},{i}"]]
                isUsed[oil_dic[f"{j},{i}"]] = 1
        
        answer = max(sum_oil, answer)
                
    
                
    
    return answer


solution([[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]])