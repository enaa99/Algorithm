

# info 10 9 8 7 6 5 4 3 2 1 0 
# 10 - i

# 라이언이 이길 수 있는 방법 중 가장 낮은 점수 많이 맞힌 경우

# n == 화살 

# 이길 수 있는 방법 찾기 
# 가장 낮은 점수 쏘기








# def cmp(arr, info):
#     result = 0
#     for i in range(11):
#         if arr[i] > info[i]:
#             result += 10-i
#     return result

# def solution(n, info):
#     answer = []
#     start = 0
#     total = 0
#     while start <= n:
#         for i in range(start, 10-n+1):
#             tempn = n
#             arr = [0] * 11
#             for j in range(i, 11):
#                 if tempn <= 0:
#                     answer = arr[:] 
#                     total = max(total, cmp(arr, info))
#                     print(answer, total)
#                 else:
#                     if tempn > info[j]:
#                         arr[j] = info[j] + 1
#                         tempn -= info[j] + 1
            
#         if tempn > 0:
#             answer = [-1]
#             print(-1)
#             break
            
#         start += 1
            
#     return answer