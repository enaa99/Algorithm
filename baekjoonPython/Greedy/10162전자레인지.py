import sys

input = sys.stdin.readline

N = int(input())

# A - 300 / B - 60 / C - 10


A = 300
B = 60
C = 10

if N%C != 0:
    print(-1)
    exit(0)

k = N//A
print(k,end=' ')

N = N%A
k = N//B
print(k,end = ' ')

N = N%B
print(N//C)