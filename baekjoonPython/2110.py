import sys


input = sys.stdin.readline
N,c = map(int,input().split())
l = [int(input()) for _ in range(N)]

l.sort()

def check(mid,k):
    tmp =0
    for i in range(1,len(l)):
        if l[i] - l[tmp] >= mid:
            tmp = i
            k -= 1
    if k <= 1: return True
    return False

def binary_serach(left,right,k):

    l,r = left,right
    
    while l +1 < r:
        mid = (r+l)//2
        
        if check(mid,k):
            l = mid
        else:
            r = mid
    return l
        
print(binary_serach(0,max(l)+1,c))