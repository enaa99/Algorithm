def solution(survey,choices):
    answer = ''
    
    # R, T
    # C, F
    # J, M
    # A, N
    
    
    
    mbti_dic ={}
    
    for i in range(len(survey)):
        if choices[i] == 4: continue
        elif choices[i] < 4:
            if mbti_dic.get(survey[i][0]):
                mbti_dic[survey[i][0]] += 1
            else:
                mbti_dic[survey[i][0]] = 1
        else:
            if mbti_dic.get(survey[i][1]):
                mbti_dic[survey[i][1]] += 1
            else:
                mbti_dic[survey[i][1]] = 1
    
    check =[['R','T'],['C','F'],['J','M'],['A','N']]
    
    for i,j in check:
        if i in mbti_dic and j in mbti_dic:
            if mbti_dic[i] >= mbti_dic[j]:
                answer += i
            else:
                answer += j
        elif i in mbti_dic and j not in mbti_dic:
            answer += i
        elif i not in mbti_dic and j in mbti_dic:
            answer += j
        else:
            answer += i
    
    
    
    return answer

solution(["AN", "CF", "MJ", "RT", "NA"],[5, 3, 2, 7, 5])