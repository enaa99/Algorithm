import sys

input = sys.stdin.readline

N = int(input())

graph = list(map(int,input().split()))



def isPrime(k):
    if k ==1 : return False
    
    for i in range(2,int(k**0.5)+1):
        if k%i ==0:
            return False
    return True


cnt = 0
for j in graph:
    if isPrime(j):
        cnt +=1

print(cnt)