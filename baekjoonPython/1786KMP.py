import sys

input = sys.stdin.readline

temp = input().rstrip()

p = input().rstrip()

pi = [0]*len(p)
def pattern():
    j = 0
    for i in range(1,len(p)):
        while j>0 and p[i] != p[j]:
            j = pi[j-1]
        if p[i] == p[j]:
            j+=1
            pi[i] = j
ans = 0
l = []
def KMP():
    global ans
    j = 0
    for i in range(len(temp)):
        while j>0 and temp[i] != p[j]:
            j = pi[j-1]
        if temp[i] == p[j]:
            if j == len(p)-1:
                j = pi[j]
                ans += 1
                l.append(i-len(p)+2)
            else:
                j+=1

pattern()
KMP()
print(ans)
for i in l:
    print(i)