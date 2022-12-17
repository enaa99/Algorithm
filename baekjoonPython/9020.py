import sys

# 소수 판별
def isPrime(n)->bool:
    for i in range(2,int(n**0.5)+1):
        if n%i ==0: return False

    return True


for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    a,b = n//2,n//2
    while a>0:
        if isPrime(a) and isPrime(b):
            print(a,b)
            break
        a-=1
        b+=1