import sys

input = sys.stdin.readline

N = input().rstrip()

q = []


# 바깥에 누가 감싸는지에 따라
tmp = 1
answer = 0
for i in N:
    if i == '[':
        q.append(i)
        tmp *= 3
    elif i == '(':
        q.append(i)
        tmp *= 2
    elif i== ')':
        if not q or q[-1] == '[':
            print(0)
            exit(0)
        if q[-1] == '(':
            answer += tmp
        q.pop()
        tmp //= 2
    else:
        if not q or q[-1] == '(':
            print(0)
            exit(0)
        if q[-1] == '[':
            answer += tmp
        q.pop()
        tmp //=3

if q:
    print(0)
else:
    print(answer)