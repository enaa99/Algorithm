import sys

input = sys.stdin.readline


n = int(input())
l= list(sorted(map(int,input().split())))

answer = [0,0]
def solv(left,right):
    
    low = left
    high = right
    ans = sys.maxsize

    while low < high:
        mid = l[low]+l[high]
        
        if abs(mid) < ans:
            answer[0],answer[1] = l[low],l[high]
            ans = abs(mid)
        
        if mid == 0:
            break
        if mid > 0:
            high -= 1
        else:
            low += 1

solv(0,n-1)
answer.sort()
print(*answer)