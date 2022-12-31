import sys

input = sys.stdin.readline

N,M = map(int,input().split())

cards = list(map(int,input().split()))

cards.sort()


ans = sys.maxsize
def binary_search(k,v):
    global ans
    low = k 
    high = len(cards)-1
    
    
    while low < high:
        mid = cards[low] + cards[high] + v
        # check
        if mid == M:
            print(M)
            exit(0)
        elif mid < M:
            low += 1
            ans = min(ans,abs(M-mid))
        else:
            high -=1


for i in range(len(cards)):
    binary_search(i+1,cards[i])

print(M-ans)