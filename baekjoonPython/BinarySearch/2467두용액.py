import sys

input = sys.stdin.readline

n = int(input())

graph = list(map(int,input().split()))



answer = [0,0]

def binary_search(left,right):
    ans = sys.maxsize
    
    l = left
    r = right
    
    while l < r:
        mid = graph[l] + graph[r]
        
        if ans > abs(mid):
            answer[0] , answer[1] = graph[l] , graph[r]
            ans = abs(mid)
        
        if mid == 0:
            break
        elif mid < 0:
            l += 1
        else:
            r -= 1
        
binary_search(0,n-1)
print(*answer,sep=" ")