import sys

def Count(n):
    cnt = 99
    
    if n < 100:
        return n
    
    for i in range(100,n+1):
        a = int(i/100)
        b = int(i%100/10)
        c = i%10

        if (a-b) == (b-c): 
            cnt+=1
    
    
    return cnt

n = int(sys.stdin.readline())
ans = Count(n)


print(ans)

#자리수 구하기
def func(n):
    for i in n+1:
        arr = list(map(int,str(n))) #1~n까지 자리수를 배열화