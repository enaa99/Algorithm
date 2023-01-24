import sys

input = sys.stdin.readline

stick = input().rstrip()

s = []
b = 0

for i in range(len(stick)):
    if stick[i] == '(':
        s.append('(')
    else:
        if stick[i-1] =='(':
            s.pop()
            b += len(s)
        else:
            s.pop()
            b +=1

print(b)