import sys

input = sys.stdin.readline

V,E = map(int,input().split())

l = []
for _ in range(E):
    a,b,c = map(int,input().split())
    l.append((a,b,c))
    
l.sort(key=lambda x:x[2])

parent =[i for i in range(V+1)]

ans = 0

def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]

def union(a,b):
    ra = find(a)
    rb = find(b)
    
    if ra > rb : parent[ra] = rb
    else: parent[rb] = ra


for x,y,z in l:
    if find(x) != find(y):
        union(x,y)
        ans += z

print(z)