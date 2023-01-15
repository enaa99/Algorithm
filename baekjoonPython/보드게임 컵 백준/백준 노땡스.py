import sys

N = int(input())
cards = list(map(int,input().split()))

ans = [cards[0]]
for i in range(1,N):
    if cards[i-1] != cards[i] -1:
        ans.append(cards[i])
    

print(sum(ans))