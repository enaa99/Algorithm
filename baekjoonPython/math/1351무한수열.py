import sys

input = sys.stdin.readline

N,P,Q = map(int,input().split())

A = {}

# A[0] = 1


# for i in range(1,N+1):
#     A[i] = A[i//P] + A[i//Q]

# print(A[N])

def recursion(k):
    if k == 0:
        return 1
    elif A.get(f'{k}') != None:
        return A[f'{k}']
    A[f'{k}'] = recursion(k//P) + recursion(k//Q)
    
    return A[f'{k}']

print(recursion(N))