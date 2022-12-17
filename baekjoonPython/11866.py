import sys


input = sys.stdin.readline

N,K = map(int,input().split())

l = [i for i in range(1,N+1)]

cnt = 0
k =[]
while len(l) >0:
    tmp = l.pop(0)
    cnt += 1
    if cnt%K != 0:
        l.append(tmp)
        continue
    k.append(str(tmp))
print(f'<{", ".join(map(str,k))}>')
