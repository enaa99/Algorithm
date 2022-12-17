import sys

input = sys.stdin.readline


# 가게이름 N, 길이 L
N,L = map(int,input().split())

l = [input().strip() for _ in range(N)]

tmp = list(l[0])



cnt = [0]*L
temp =[0]*N

for i in range(L):
    for j in range(1,N):
        if tmp[i] != l[j][i]:
            cnt[i] +=1
            temp[j] += 1
    
    for k in temp:
        if k > 2:
            print('CALL FRIEND')
            exit(0)
    if cnt[i] == N-1:
        tmp[i] = l[-1][i]
        #바꾸기작업

print("".join(tmp))