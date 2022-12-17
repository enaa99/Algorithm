import sys


# 서치후 이진탐색
def binary_search(a:list,left,right,k):
    
    l = left
    r = right-1
        
    while l<=r:
        mid = (l+r)//2
        if a[mid] == k: return True
        
        elif k < a[mid]: 
            r = mid-1

        else: # k >a[mid] 
            l = mid+1
    return False



input = sys.stdin.readline
n = int(input())

a = list(map(int,input().split()))
a.sort()

kk = int(input())
lm = list(map(int,input().split()))
for i in lm:
    if binary_search(a,0,len(a),i):
        print(1)
        continue
    print(0)
    



