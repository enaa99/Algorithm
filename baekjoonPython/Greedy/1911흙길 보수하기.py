import sys

input = sys.stdin.readline

N,L = map(int,input().split())

l = [list(map(int,input().split())) for _ in range(N)]
l.sort()


cnt = 0
j = 0
i = 0
while j < l[-1][1]-1:
    if j < l[i][0]:
        j = l[i][0]
        cnt += 1
        j += L - 1
        while j<l[i][1]-1:
            j += L
            cnt += 1
    else:
        while j < l[i][1]-1:
            j += L      
            cnt += 1
    i +=1
print(cnt)