import sys

input = sys.stdin.readline


# 사대 수, 동물 수, 사정거리
M,N,L = map(int,input().split())

# 사대 위치
shoot = list(map(int,input().split()))
shoot.sort()
cnt = 0
dist = L-1
# 동물 위치

def kill(left,right,a,b):
    l = left
    r = right
    global cnt
    while l<=r:
        mid = (l+r)//2
        low = a + b -L
        high = L - b + a
        
        if shoot[mid] >= low and shoot[mid] <= high:
            cnt +=1
            break
        if shoot[mid] < low:
            l = mid +1
        else:
            r = mid -1



for _ in range(N):
    a,b = map(int,input().split())
    
    if b > L:continue
    kill(0,M-1,a,b)

print(cnt)