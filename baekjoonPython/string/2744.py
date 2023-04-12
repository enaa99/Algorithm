import sys

input = sys.stdin.readline

N = list(input().rstrip())


for i in range(len(N)):
    if N[i].isupper():
        N[i] =N[i].lower()
    else:
        N[i] = N[i].upper()
print(''.join(N))