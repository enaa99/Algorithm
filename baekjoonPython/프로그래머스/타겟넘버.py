# def solution(numbers, target):
#     answer = DFS(numbers, target, 0)
#     return answer

# def DFS(numbers, target, depth):
#     answer = 0
#     if depth == len(numbers):
        
#         if sum(numbers) == target:
#             return 1
#         else: return 0
#     else:
#         answer += DFS(numbers, target, depth+1)
#         numbers[depth] *= -1
#         answer += DFS(numbers, target, depth+1)
#         return answer

from collections import deque
def solution(numbers,target):
    answer = 0
    
    q = deque()
    
    q.append([0,0])
    while q:
        v,d = q.popleft()
        
        if d == len(numbers) :
            if v == target:
                answer +=1
            continue
        
        q.append([v + numbers[d],d+1])
        q.append([v - numbers[d],d+1])
        
    
    return answer

solution([1,1,1,1,1],3)