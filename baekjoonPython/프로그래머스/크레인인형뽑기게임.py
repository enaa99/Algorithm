def solution(board,moves):
    answer = 0
    bucket = []
    
    # moves 위에서 부터 내려온다
    
    for move in moves:
        move -= 1 
        for x in range(len(board)):
            if board[x][move] != 0:
                bucket.append(board[x][move])
                board[x][move] = 0
                break
        if bucket and len(bucket) > 1:
            cmp = bucket[-2]
            while bucket:
                answer +=1
                v = bucket.pop()
                if v == cmp:
                    bucket.pop()
                    answer +=1
                else:
                    bucket.append(v)
                    answer -=1
                    break
                
    return answer

solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4])