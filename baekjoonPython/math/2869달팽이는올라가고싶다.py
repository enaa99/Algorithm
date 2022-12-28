import sys

A,B,V = map(int,input().split())

d = (V-B)//(A-B) if (V-B)%(A-B) == 0 else (V-B)//(A-B) + 1 

print(d)