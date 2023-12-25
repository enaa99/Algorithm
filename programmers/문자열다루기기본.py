def solution(s):
    if len(s) != 4 and len(s) != 6:
        return False
    
    for i in s:
        if i.isalpha():
            return False
    return True