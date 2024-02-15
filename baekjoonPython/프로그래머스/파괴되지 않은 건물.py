from collections import deque
def solution(board, skill):
    answer = 0
    
    # type 1 공격 / type 2 회복
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    
    def BFS(ty, x1,y1, x2,y2, degree):
        
        isVisited = [[0]*len(board[0]) for _ in range(len(board))]
        
        q = deque()
        q.append([x1,y1])
        if ty == 1:
            degree *= -1
        while q:
            x,y = q.popleft()
            for i in range(4):
                xa = dx[i] + x
                ya = dy[i] + y
                
                
                if xa < 0 or ya < 0 or xa>=len(board) or ya>= len(board[0]) : continue
                if xa >x2 or xa < x1 or ya>y2 or ya<y1 or isVisited[xa][ya]: continue
                
                isVisited[xa][ya] = 1
                board[xa][ya] += degree
                q.append([xa,ya])
                
    
    for type, r1, c1, r2, c2, degree in skill:
        BFS(type, r1,c1, r2,c2,degree)
    
    
    for i in board:
        for j in i:
            if j > 0:
                answer +=1
    
    
    return answer