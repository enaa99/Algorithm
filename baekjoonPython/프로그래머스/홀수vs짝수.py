def solution(num_list):
    answer_1 = 0
    answer_2 = 0
    
    for i in range(len(num_list)):
        if (i+1)%2 == 0:
            answer_1 += num_list[i]
        else:
            answer_2 += num_list[i]
    
    return max(answer_1,answer_2)