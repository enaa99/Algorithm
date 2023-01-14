import sys

input = sys.stdin.readline

alpha = [-1]*26

a = 'z'

S = input().rstrip()

for i in range(len(S)):
    if alpha[ord(S[i])-97] == -1:
        alpha[ord(S[i])-97] = i

print(*alpha)