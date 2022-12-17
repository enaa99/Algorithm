import sys

input = sys.stdin.readline

n,m = map(int,input().split())

parent = [i for i in range(n+1)]


def union(x,y):
    xa = find(x)
    xy = find(y)
    if xa > xy:
        parent[xa] = xy
    else:
        parent[xy] = xa

def find(x):
    if x == parent[x] : return x
    parent[x] = find(parent[x])
    return parent[x]
for _ in range(m):
    a,b,c = map(int,input().split())
    if a == 0:
        union(b,c)
    else:
        if b == c:
            print('YES')
        else:
            if find(b) == find(c):
                print('YES')
            else:
                print('NO')