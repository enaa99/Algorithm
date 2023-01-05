import sys
from itertools import permutations,combinations,product

input = sys.stdin.readline

N = int(input())

# arr = [0]*(N+1)
# isUsed = [0]*(N+1)

# def DFS(cnt):
#     if cnt == N:
#         for i in range(N):
#             print(arr[i],end = ' ')
#         print()
#         return
    
#     for i in range(1,N+1):
#         if not isUsed[i]:
#             isUsed[i] = True
#             arr[cnt] = i
#             DFS(cnt+1)
#             isUsed[i] = False

k = [i+1 for i in range(N)]

q = list(permutations(k,N))

for num in q:
    for i in num:
        print(i,end=' ')
    print()