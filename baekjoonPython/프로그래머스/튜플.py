
def solution(s):
    answer = []
    

    s = s.split('}')
    
    q = []
    for i in range(len(s)):
        if s[i]:
            q.append((s[i].replace('{','').split(',')))
    
    q.sort(key=lambda x:(len(x),x))
    
    for num in q:
        for i in num:
            if not i: continue
            if int(i) not in answer:
                answer.append(int(i))
    
    return answer



print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))