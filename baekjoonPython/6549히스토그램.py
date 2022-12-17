import sys
sys.setrecursionlimit(450000)
input = sys.stdin.readline

#l = list(map(int,input().split()))
# 1. 현재 구간을 반으로 쪼갠다.
# 2 .왼쪽 절반 구간에서의 가장 큰 직사각형과, 오른쪽 절반 구간에서의 가장 큰 직사각형의 크기를 재귀적으로 구한다.
# 3 .현재 구간에서, 아까 반으로 쪼갰던 경계 부분을 포함하는 가장 큰 직사각형의 크기를 구한다.
# 4 .셋(왼쪽 절반, 오른쪽 절반, 경계 포함)을 비교한다.

def checkHeight(left,right):
    if left == right:
        return k[left]
    
    mid = (left+right)//2
    a = checkHeight(left,mid)
    b = checkHeight(mid+1,right)
    ans = max(a,b)
    h = min(k[mid],k[mid+1])
    w = 2
    s = w*h
    
    n,m = mid,mid+1
    while left < n or m <right:
        if  m==right or left < n and k[n-1] > k[m+1]:
            n -= 1
            w +=1
            h = min(h,k[n])
            s = max(s,w*h)
        else:
            m += 1
            w += 1
            h = min(h, k[m])
            s = max(s, w * h)
    return max(ans,s)

while True:
    k = list(map(int,input().split()))
    if k[0] == 0: break
    print(checkHeight(1,k[0]))
    

