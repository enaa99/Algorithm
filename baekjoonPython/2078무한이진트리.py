import sys


input = sys.stdin.readline


a, b = map(int, input().split())

l, r = 0, 0
while a>1 or b>1:
    if a < b:
        b-=a
        r +=1
    elif a > b:
        a -=b
        l +=1
        

print(l, r)