import sys

N = int(input())

def count(k):
    cnt = 99
    if k <100:
        return k
    
    
    for i in range(100,k+1):
        a = i//100
        b = (i%100)//10
        c = i%10
        if a-b == b-c:
            cnt +=1
    
    return cnt



print(count(N))