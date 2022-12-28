import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

prime = [True for _ in range(10000)]

def isPrime():
    for i in range(2, 100):
        if prime[i] == True:
            for j in range(2*i, 10000,i):
                prime[j] = False


def BFS(start,end):
    q = deque()
    isUsed = [False for _ in range(10000)]
    isUsed[start] = True
    q.append((start,0))
    
    while q:
        low,cnt = q.popleft()
        
        strLow = str(low)
        
        if low == end: return cnt
        
        for i in range(4):
            for j in range(10):
                temp = int(strLow[:i] + str(j) + strLow[i+1:])
                
                if temp >= 1000 and not isUsed[temp] and prime[temp] :
                    isUsed[temp] = True
                    q.append((temp,cnt+1))

isPrime()

for _ in range(N):
    a, b = map(int,input().split())
    ans = BFS(a,b)
    ans = ans if ans != None else "Impossible"
    print(ans)