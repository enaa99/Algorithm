import sys

input = sys.stdin.readline

N = int(input())

k = N//4
less = N/4

long = "long "


if k == less:
    long = long*k
else:
    long = long*(k+1)

print(long+"int")