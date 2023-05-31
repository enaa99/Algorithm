# stack
def solution(numbers):
    stack = []
    answer = [0] * len(numbers)

    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
        stack.append(i)
    while stack:
        answer[stack.pop()] = -1

solution([2,3,3,5])


# def solution(numbers):
#     answer = [0]*len(numbers)
#     s = []
    
#     for i in range(len(numbers)):
#         while s and numbers[s[-1]] < numbers[i]:
#             answer[s.pop()] = numbers[i]
#         s.append(i)
        
#     while s:
#         answer[s.pop()] = -1
    
#     return answer