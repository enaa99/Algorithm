def solution(s):
    answer = len(s)
    
    # bruteForce로 모두탐색?
    for i in range(1,len(s)//2 + 1):
        # i 길이만큼 잘라 압축한다
        # 같다면 i만큼 밀어서 비교
        # 다르다면 1 만큼 밀어서 비교
        tmp,idx ='',0
        while idx < len(s):
            c,n = s[idx:idx+i],1
            while c == s[idx+i: idx+i+i]:
                idx += i
                n += 1
            tmp += str(n) + c if n!=1 else c
            idx += i
        answer = len(tmp) if len(tmp) < answer else answer
    
    
    
    return answer