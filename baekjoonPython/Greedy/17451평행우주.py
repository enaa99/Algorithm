import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
l.reverse()
answer = 0
for i in range(n):
    if answer <= l[i]:
        answer = l[i]
    else:
        if answer % l[i]:
            answer = (answer // l[i] + 1) * l[i]
print(answer)