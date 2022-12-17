import sys

number = "1924"

def solution(number, k):
    answer = ''
    
    
    l = [number[0]]
    i = 1
    while True:
        if l[-1] > number[i]:
            l.append(number[i])
            i += 1
        else:
            while l[-1] <= number[i] and k>0: 
                l.pop()
                k -= 1
                if not l:break
            l.append(number[i])
            i+=1
        if i == len(number) -1 : break
            
    for i in l:
        answer += i
        
solution(number,2)