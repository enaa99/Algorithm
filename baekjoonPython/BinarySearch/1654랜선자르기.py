import sys

input = sys.stdin.readline

K, N = map(int,input().split())

# 가지고 있는 랜선으로 N개의 같은 길이 최대 랜선


l = [int(input()) for _ in range(K)]

def check(k):
    sum = 0
    for i in l:
        sum += i//k
    return sum

def binary_search(left,right):
    l = left
    r = right
    while l + 1< r:
        mid = (l+r)//2
        tmp = check(mid)
        if tmp < N:
            r = mid 
        else:
            l = mid 
    return l


print(binary_search(0,max(l)+1))
