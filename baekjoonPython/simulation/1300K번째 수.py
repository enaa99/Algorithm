import sys

input = sys.stdin.readline

N = int(input())

k = int(input())

# 크기 N*N 배열 A
# 배열 들어 있는 수 A[i][j] = i*j

# B에 넣으면 B의 크기 N*N 1차원배열

# P(x)는 'N*N 배열에서 x 이하의 수가 k개 이상 있다'
def check(value):
    result = 0
    for i in range(1,N+1):
        result += min(value//i,N)
    return result

def binary_search():
    l = 0
    r = k+1
    
    while l+1 < r:
        mid = (l+r)//2
        tmp = check(mid)
        
        if tmp < k:
            l = mid
        else:
            r = mid
            
    return r

print(binary_search())









