def solution(n):
    triangle = [ [0] * n for _ in range(n)]
    answer = []
    
    draw(triangle, n)
    
    for num in triangle:
        for count in num:
            if count != 0:
                answer.append(count)
    
    return answer

def draw(triangle, n):
    x, y = -1, 0
    num = 1
    for i in range(n):
        for j in range(i,n):
            if i%3 == 0:
                x +=1
            elif i%3 == 1:
                y += 1
            else:
                x -= 1
                y -= 1
            triangle[x][y] = num
            num+=1
            
    