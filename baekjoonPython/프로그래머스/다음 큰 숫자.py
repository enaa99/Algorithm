def solution(n):
    answer = 0
    
    
    b = bin(n)
    cnt = b.count('1')
    
    n += 1
    while True:
        b = bin(n)
        k = b.count('1')
        if k == cnt:
            return n
        n +=1
    



solution(78)