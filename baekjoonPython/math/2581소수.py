import sys

input = sys.stdin.readline

M = int(input())

N = int(input())

prime =[False]*100001
prime[0]=prime[1] =True 


def isPrime():
    for i in range(2,len(prime)):
        if not prime[i]:
            for j in range(i*2,len(prime),i):
                prime[j] = True


isPrime()

q = []
for i in range(M,N+1):
    if not prime[i]:
        q.append(i)

if q:
    print(sum(q))
    print(q[0])
else:
    print(-1)
