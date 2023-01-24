import string
n = int(input())
strn = list(input())
alpha = [0] * n
for i in range(n):
    alpha[i] = (int(input())) 
stack=[]

for s in strn:
    if s.isalpha():
        stack.append(alpha[ord(s) - ord('A')])
    else:
        n2 = stack.pop()
        n1 = stack.pop()
        if s == '+' :
            stack.append(n1+n2)
        elif s == '-':
            stack.append(n1-n2)
        elif s == '*':
            stack.append(n1*n2)
        elif s == '/':
            stack.append(n1/n2)
print(format(stack[0], ".2f"))
