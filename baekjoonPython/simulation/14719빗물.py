import sys

input = sys.stdin.readline


H,W = map(int,input().split())

height = list(map(int,input().split()))
answer = 0

# H 세로 W 가로

for i in range(1,W-1):
    l = r = 0
    for j in range(i):
        l = max(height[j],l)
    for k in range(W-1,i,-1):
        r = max(r,height[k])
        
    answer += max(0,min(l,r) - height[i])

print(answer)