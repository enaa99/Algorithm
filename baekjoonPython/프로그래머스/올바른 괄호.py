def solution(s):
    
    
    q = []
    for i in s:
        if i == ')':
            if q and q[-1] == '(':
                q.pop()
            else:
                return False
        else:
            q.append('(')
    
    if q:
        return False
    else:
        return True
    
