import sys

n,r,c = map(int,sys.stdin.readline().split())
cnt = 0

def FindZ(k,r,c):
    if k == 0:
        return 0
    
    return 2*(r%2)+(c%2) + 4*FindZ(k-1,r//2,c//2)


def DFS(x,y,n):
    global cnt
    if x>r or x+n <= r or y>c or y+n <= c:
        cnt += n**2
        return
    
    if n>2:
        n//=2
        DFS(x,y,n)
        DFS(x,y+n,n)
        DFS(x+n,y,n)
        DFS(x+n,y+n,n)
    else :
        if x == r and y == c:
            print(cnt)
        elif x == r and y+1 == c:
            print(cnt + 1)
        elif x+1 == r and y == c:
            print(cnt+2)
        else:
            print(cnt + 3)
        sys.exit()
    
    return

DFS(0,0,2**n)


# print(FindZ(n,r,c))
