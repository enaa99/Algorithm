import sys

input = sys.stdin.readline

N = int(input())

num = [1 for i in range(10)]


for i in range(N-1):
    for j in range(1,10):
        num[j] = num[j-1] +num[j]

print(sum(num)%10007)


