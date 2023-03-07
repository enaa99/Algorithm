from collections import defaultdict

def solution(n,words):
    answer = [0,0]
    
    word_dic = defaultdict(int)
    
    tmp = 0
    for i in range(len(words)):
        if i%n == 0:
            tmp += 1
        word_dic[words[i]] += 1 
        if word_dic[words[i]] != 1:
            answer[0]= i%n+1
            answer[1] = tmp
            break
        
        if i != 0:
            if words[i-1][-1] != words[i][0]:
                answer[0]= i%n+1
                answer[1] = tmp
                break
    
    
    
    return answer

solution(	2, ["hello", "one", "even", "never", "now", "world", "draw"])