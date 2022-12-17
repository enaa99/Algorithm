import sys

input = sys.stdin.readline

# - 뒤, - 앞 

l = input().split('-')


tmp = []

for i in l:
    cnt = 0
    splits = i.split('+')
    for j in splits:
        cnt += int(j)
    tmp.append(cnt)
ans = tmp[0]
for i in range(1,len(tmp)):
    ans -= tmp[i]

print(ans)









