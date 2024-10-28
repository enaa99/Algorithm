def solution(myString, pat):
    answer = ''

    check = ''
    for i in range(len(myString)-1, -1, -1):
        check += myString[i]
        if pat in check[::-1]:
            return myString[:i+len(pat)]
    
    
    return answer