import sys

input = sys.stdin.readline


l = [[0]*101 for _ in range(101)]

sum = 0
for i in range(4):
    a,b,c,d = map(int,input().split())
    for j in range(a,c):
        for k in range(b,d):
            if l[j][k] == 0:
                l[j][k] = 1
                sum += 1

print(sum)