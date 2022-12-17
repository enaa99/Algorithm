import sys

input = sys.stdin.readline

N = int(input())

l =list(map(int,input().split()))

s =[(1,l[0])]
ans = [0]

for i in range(1,N):
    if l[i] <= s[-1][1]:
        ans.append(s[-1][0])
        s.append((i+1,l[i]))
        continue
    while len(s) > 0 :
        s.pop()
        
        if len(s) <= 0:
            ans.append(0)
            s.append((i+1,l[i]))
            break
        if l[i] <= s[-1][1]:
            ans.append(s[-1][0])
            s.append((i+1,l[i]))
            break

print(*ans)