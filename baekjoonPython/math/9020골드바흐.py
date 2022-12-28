import sys

input = sys.stdin.readline

N = int(input())

def isPrime(k):
    for i in range(2,int(k**0.5)+1):
        if k%i == 0:
            return False
    return True


for _ in range(N):
    k = int(input())
    
    a,b = k//2,k//2
    while not isPrime(a) or not isPrime(b):
        a -= 1
        b += 1
    print(a,b)