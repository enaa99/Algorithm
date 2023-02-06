import sys

input = sys.stdin.readline

N = input().rstrip()

for i in range(len(N)):
    if i%10 == 0 and i != 0:
        print()
    print(N[i],end="")