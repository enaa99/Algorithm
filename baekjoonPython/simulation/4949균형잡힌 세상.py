import sys

input = sys.stdin.readline

while True:
    S = input().rstrip()
    
    if S == '.':
        break
    
    tmp = []
    
    flag = 0
    for i in S:
        if i == '(' or i == '[':
            tmp.append(i)
        elif i == ')':
            if tmp and tmp[-1] == '(':
                tmp.pop()
            else:
                flag = 1
                break
        elif i == ']':
            if tmp and tmp[-1] == '[':
                tmp.pop()
            else:
                flag = 1
                break
    if not flag:
        if tmp:
            print('no')
        else:
            print('yes')
    else:
        print('no')