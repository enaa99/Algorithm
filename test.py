def solution(s):
    q= []
    for i in s:
        if i ==')':
            if q and q[-1] == '(':
                q.pop()
            else:
                return False
        else:
            q.append(i)
    if q:
        return False
            

    return True

# 뒤에 있는 큰 수 찾기

solution('()()')