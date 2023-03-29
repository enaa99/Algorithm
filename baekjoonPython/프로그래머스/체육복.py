def solution(n, lost, reserve):
    answer = n
    
    students = [1 for _ in range(n+1)]
    
    for i in lost:
        students[i] -=1
    
    for i in reserve:
        students[i] += 1
    
    
    for i in range(len(students)):
        if students[i] == 0:
            if i == 0 :
                if students[i+1] > 1:
                    students[i+1] -=1
                else:
                    answer -=1
            elif i == len(students)-1:
                if students[i-1] > 1:
                    continue
                else:
                    answer -=1
            else:
                if students[i-1] > 1:
                    continue
                elif students[i+1] > 1:
                    students[i+1] -=1
                else:
                    answer -=1
    
    return answer

solution(5,[2,4],[1,3,5])