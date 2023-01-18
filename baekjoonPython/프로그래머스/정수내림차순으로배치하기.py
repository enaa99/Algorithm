def solution(n):
    answer = 0
    s = list(str(n))
    s.sort(reverse=True)
    print()
    
    return ''.join(s)

solution(118372)