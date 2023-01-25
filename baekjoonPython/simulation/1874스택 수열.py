import sys


input = sys.stdin.readline

n = int(input())

array =[int(input()) for _ in range(n)]

s = []
answer = []
j = 0
for i in range(1,n+1):
    s.append(i)
    answer.append('+')
    
    while array[j] == s[-1]:
        s.pop()
        answer.append('-')
        j += 1
        if not s: break

if not s:
    print(*answer,sep ='\n')
else:
    print('NO')