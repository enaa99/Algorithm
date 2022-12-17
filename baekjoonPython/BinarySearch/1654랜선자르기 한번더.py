import sys

input = sys.stdin.readline


# K 랜선의 개수, 필요한 랜선 N
K,N = map(int,input().split())

l = [int(input()) for _ in range(K)]

def check(k):
    ans = 0
    for i in l:
        ans += i//k
    return ans




def binarySearch(left,right):
    l = left
    r = right
    
    while l+1 < r:
        mid = (l+r)//2
        
        if check(mid) < N:
            r = mid
        else:
            l= mid
            
    return l

print(binarySearch(0,max(l)+1))