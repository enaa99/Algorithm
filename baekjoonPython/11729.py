import sys

input = sys.stdin.readline

N = int(input())




print(2**N - 1)
def hanoi(cnt,a,b,c):
    if cnt==1:
        print(a,c)
        return    
    
    hanoi(cnt-1,a,c,b)
    hanoi(1,a,b,c)
    hanoi(cnt-1,b,a,c)
hanoi(N,1,2,3)