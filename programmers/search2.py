from collections import deque
def solution(board):
    answer = -1
    
    move = [[0,1],[1,0],[-1,0],[0,-1]]
    
    def check(x,y,direction):
        q= deque()
        q.append([x,y])
        count = 0
        
        while q:
            a,b = q.popleft()
            xa = a+direction[0]
            ya = b+direction[1]
            
            if xa<0 or ya<0 or xa>=8 or ya>=8: break
            if board[xa][ya] ==2:
                count +=1
                q.append([xa,ya])
                
            elif board[xa][ya]==0:
                return count
    for i in range(8):
        for j in range(8):
            if board[i][j] ==1:
                count = 0
                for k in move:
                    count+= check(i,j,k)
                answer = max(count,answer)
    return answer

solution([[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,1,1,0,0,0],[0,0,0,1,0,0,0,0],[0,0,1,1,2,0,0,0],[0,0,2,2,2,0,0,0],[0,0,0,0,2,1,0,0],[0,0,0,0,0,0,0,0]])