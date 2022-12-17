import sys

input = sys.stdin.readline


s = [0]
for _ in range(int(input())):
    k = int(input())
    for i in range(len(s)-1,-1,-1):
        if s[i] <= k: s.pop()
        else : break
    s.append(k)
print(len(s))
