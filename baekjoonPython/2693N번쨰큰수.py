import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    l = list(map(int,input().split()))
    l.sort(key=lambda x:-x)
    print(l[2])