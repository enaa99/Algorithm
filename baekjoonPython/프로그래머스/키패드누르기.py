import heapq
def solution(numbers,hand):
    answer = ''
    
    # 상하좌우로만 이동가능
    
    phone = [[0]*3 for _ in range(4)]
    
    j = 0
    for i in range(4):
            phone[i][0],phone[i][1],phone[i][2] = str(1+j),str(2+j),str(3+j)
            j +=3
    
    phone[-1][0],phone[-1][1] ,phone[-1][2] = '*','0','#'
    
    
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    
    def bfs(start,end):
        q = []
        q.append([0,start[0],start[1]])
        isUsed = [[0]*3 for _ in range(4)]
        if start == end: return 0
        while q:
            d,x,y = heapq.heappop(q)
            for i in range(4):
                xa = x + dx[i]
                ya = y + dy[i]
                
                if xa < 0 or ya < 0 or xa>= 4 or ya >= 3 or isUsed[xa][ya]: continue
                if phone[xa][ya] == '*' or phone[xa][ya] =='#': continue
                if [xa,ya] == end:
                    return d+1
                
                isUsed[xa][ya] = 1
                heapq.heappush(q,[d+1,xa,ya])
    
    def findPos(k):
        for i in range(4):
            for j in range(3):
                if phone[i][j] == k:
                    return [i,j]
    
    
    l_start = [3,0]
    r_start = [3,2]
    button_left = ['1','4','7']
    button_right =['3','6','9']
    for num in numbers:
        if str(num) in button_left:
            answer +='L'
            l_start = [button_left.index(str(num)),0]
        elif str(num) in button_right:
            answer +='R'
            r_start = [button_right.index(str(num)),2]
        else:
            end = findPos(str(num))
            l_d = bfs(l_start,end)
            r_d = bfs(r_start,end)
            if l_d > r_d:
                answer += 'R'
                r_start = end
            elif l_d < r_d:
                answer += 'L'
                l_start = end
            else:
                if hand == 'right':
                    answer += 'R'
                    r_start = end
                else:
                    answer += 'L'
                    l_start = end

    
    return answer


solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right")