import sys
from collections import Counter

input = sys.stdin.readline

M = int(input())

cards = list(map(int,input().split()))

N = int(input())

finds = list(map(int,input().split()))


card = Counter(cards)

for i in finds:
    print(card[i],end =' ')