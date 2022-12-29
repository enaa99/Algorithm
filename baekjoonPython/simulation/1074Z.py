import sys

n,r,c = map(int,sys.stdin.readline().split())


def FindZ(k,r,c):
    if k == 0:
        return 0
    
    return 2*(r%2)+(c%2) + 4*FindZ(k-1,r//2,c//2)


print(FindZ(n,r,c))