from collections import defaultdict
def solution(name, yearning, photo):
    answer = []
    len_dic = len(name)
    dict_photo = defaultdict(int)
    
    for i in range(len_dic):
        dict_photo[name[i]] = yearning[i]
    
    for num in photo:
        k = 0
        for i in num:
            k += dict_photo[i]
        answer.append(k)
    
    return answer