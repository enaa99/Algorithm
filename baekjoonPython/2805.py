# import sys

# input = sys.stdin.readline

# n,m = map(int,input().split())

# l = list(map(int,input().split()))


# def binary_search(left,right):
#     l = left
#     r = right
    
#     if l+1 < r:
#         mid = (l+r)//2
        
#         tmp = check(mid)
#         if tmp : l = mid
#         else : r = mid
        
#         binary_search(l,r)
#     else:
#         print(l)


# def check(k):
#     sum = 0
#     for j in l:
#         if j > k:
#             sum += j -k
#     if sum >= m : return True
#     return False

# binary_search(0,max(l))

import sys

input = sys.stdin.readline

n,m = map(int,input().split())

l = list(map(int,input().split()))


def binary_search(left,right):
    l = left
    r = right
    
    if l+1 < r:
        tmp =0
        mid = (l+r)//2
        
        tmp = check(mid)
        
        if tmp >= m: l = mid
        else :#tmp < m 
            r = mid
        binary_search(l,r)
    else:
        print(l)

def check(k):
    sum = 0
    for j in l:
        if j > k:
            sum += j -k
    return sum

binary_search(0,max(l))