# import sys
# from itertools import combinations

# input = sys.stdin.readline
# answer = 0
# n, s = map(int, input().split())
# arr = list(map(int, input().split()))

# for i in range(1, n + 1):
#     comb = list(combinations (arr, i))
#     for c in comb:
#         if sum(c) == s:
#             answer += 1

# print(answer)


# #메모리 초과===============================
# import sys
# sys.setrecursionlimit(10**6)


# n,s = map(int,sys.stdin.readline().split())

# arr = list(map(int,sys.stdin.readline().split()))

# ans = 0


# def check(cnt,val,num):
#     global ans
#     if val == s:
#         ans += 1
#         return
    
#     for i in range(num,n):
#         if val != s:
#             check(cnt+1,val+arr[i],i)
    
# check(0,0,0)
# print(ans)

# safe 메모리=================================
#=============================================
n, s = map(int, input().split())
arr = list(map(int, input().split()))


def func(idx, d):
    global cnt
    if (idx == n):
        if (s == d):
            cnt += 1
            return
    else: 
        func(idx + 1, d + arr[idx])
        func(idx + 1, d)

cnt = 0
func(0, 0)

if (s == 0):
    cnt -= 1
print(cnt)