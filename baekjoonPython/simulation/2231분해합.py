import sys

input = sys.stdin.readline

N = int(input())

for i in range(1,N+1):
    tmp = str(i)
    sum = i
    for j in tmp:
        sum += int(j)
    
    if sum == N:
        print(i)
        exit(0)


print(0)
