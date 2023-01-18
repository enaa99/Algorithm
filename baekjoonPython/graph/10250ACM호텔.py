import sys

input = sys.stdin.readline

T = int(input())

# H,W,N

for i in range(T):
    h,w,n = map(int,input().split())
    
    k = n//h
    less = n%h*100 if n%h*100 !=0 else h*100-1
    
    answer = k+less+1
    print(answer)