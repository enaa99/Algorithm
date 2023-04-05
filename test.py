def solution(s):
    
    def check(l,r):
        tmp = 0
        while l >=0 and r < len(s):
            if s[l] == s[r]:
                tmp += 0
                l -=1
                r +=1
            else:
                break
        return tmp
    
    
    answer = 0
    for i in range(len(s)):
        answer += check(i,i+1)
        answer += check(i,i)

    return answer

# 뒤에 있는 큰 수 찾기

solution('()()')