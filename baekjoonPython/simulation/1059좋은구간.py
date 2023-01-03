import sys

input = sys.stdin.readline

N = int(input())

l = list(map(int,input().split()))

k = int(input())

arr = [0,0]

if k in l:
    print(0)
    exit()

l.append(k)
l.sort()

ans = 0
tmp = l.index(k)

start = end = 0

if tmp == 0:
    start = 1
    end = l[1]
elif tmp == len(l)-1:
    start = l[-2]+1
    end = l[-1]
else:
    start = l[tmp-1]+1
    end = l[tmp+1]


for i in range(start,k+1):
    for j in range(k,end):
        if i == j: continue
        ans +=1 

print(ans)