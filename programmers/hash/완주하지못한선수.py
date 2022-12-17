import sys

input = sys.stdin.readline

n = int(input())
times = list(map(int,input().split()))

def solution(n,times):
    
    l = 0
    r = max(times)*n + 1
    
    while l+1<r:
        mid = (l+r)//2 
        if check(mid):
            r = mid
        else:
            l = mid
                
    return l+1

def check(mid):
    cnt = n
    for i in times:
        k = mid//i
        cnt -= k
        if cnt <=0 : return True
    return False


print(solution(n,times))