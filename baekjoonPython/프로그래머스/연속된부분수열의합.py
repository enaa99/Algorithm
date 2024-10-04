def solution(sequence, k):
    answer = []

    
    for i in range(len(sequence)):
        sum = sequence[i]
        for j in range(i, len(sequence)):
            if i == j: 
                if sum == k:
                    answer.append([i,i])
                continue
            sum += sequence[j]
            if sum > k:
                break
            if sum == k:
                answer.append([i,j])
            
    answer.sort(key=lambda x:abs(x[1]-x[0]))
    return answer[0]



def solution(sequence, k):
    answer = []
    
    sum = 0
    n = len(sequence)
    end = 0
    for i in range(n):
        
        while sum < k and end < n:
            sum += sequence[end]
            end += 1
        
        if sum == k:
            answer.append([i, end-1, end-1-i])
        
        sum -= sequence[i]
    answer.sort(key=lambda x:x[2])
    return answer[0][:2]