import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    k = input().rstrip()
    
    a,b = k.split(',')
    
    print(int(a)+int(b))