# import sys

# input = sys.stdin.readline

# N,C = map(int,input().split())


# bags = list(map(int,input().split()))
# # bags.insert(0,0)

# # dp = [0]*(C+1)


# # dp[0] = 1
# # ans = 1
# # for i in range(N):
# #     for j in range(C+1):
# #         if bags[i] <= j:
# #             ans += 1

# # print(ans)


# # 가방에 넣는 방법의 수
# # 무게 


# def check(k):
#     ans = 1
#     for i in range(N):
#         if bags[i] <= k:
#             ans +=1


# def binary_search():
#     l = 0
#     r = C+1
    
#     while l+1 < r:
#         mid = (l+r)//2
#         tmp = check(mid)


import sys
from itertools import combinations

input = sys.stdin.readline

n, c = map(int, input().split())
arr = list(map(int, input().split()))

# meet in the middle
arr_1 = arr[:n//2]
arr_2 = arr[n//2:]

subsum_a = []
subsum_b = []

for i in range(len(arr_1) + 1):
    comb_a = combinations(arr_1, i)

    for comb in comb_a:
        subsum_a.append(sum(comb))
        
for i in range(len(arr_2) + 1):
    comb_b = combinations(arr_2, i)
    
    for comb in comb_b:
        subsum_b.append(sum(comb))

subsum_a.sort()
ans = 0

# subsum_a와 subsum_b의 값을 더하는 작업을 이분탐색으로 진행
for element_b in subsum_b:

    # 이미 subsum_b의 값이 c를 넘었다면 작업 X
    if element_b > c:
        continue
    
    start = 0
    end = len(subsum_a) 

    while start + 1 < end:
        mid = (start + end) // 2

        if subsum_a[mid] + element_b > c:
            end = mid
        
        else:
            start = mid
    
    ans += end

print(ans)