import sys

input = sys.stdin.readline

N = input().rstrip()


if N[0] == '0':
    if N[1] == 'x':
        N = int(N,16)
    else:
        N = int(N,8)


print(N)


