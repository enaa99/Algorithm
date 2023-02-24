from collections import defaultdict

def solution(keymap, targets):
    answer = []
    key_dic = defaultdict(int)
    
    
    for key in keymap:
        for i in range(len(key)):
            if key_dic[key[i]] == 0:
                key_dic[key[i]] = i+1
            else:
                key_dic[key[i]] = min(key_dic[key[i]],i+1)
    
    
    for num in targets:
        tmp = 0
        for i in num:
            if key_dic[i] == 0:
                tmp = -1
                break
            tmp += key_dic[i]
        
        answer.append(tmp)
        
    
    return answer


solution(["AA"],["B"])