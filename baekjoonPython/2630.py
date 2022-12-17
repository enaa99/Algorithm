import sys

input = sys.stdin.readline

N = int(input())

l = [[0 for _ in range(N)]for i in range(N)]

white = 0
blue  = 0

for i in range(N):
        k = list(map(int,input().split()))
        for j in range(N):
            l[i][j] = k[j]
            

def divide(n,x,y):
    global blue
    global white
    tmp = l[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if tmp != l[i][j]:
                divide(n//2,x,y)
                divide(n//2,x+n//2,y)
                divide(n//2,x,y+n//2)
                divide(n//2,x+n//2,y+n//2)
                return
    if tmp == 1: blue +=1
    else: white +=1
    
    
divide(N,0,0)
print(white,blue,sep='\n')