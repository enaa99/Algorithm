import sys

input = sys.stdin.readline

V, E = map(int,input().split())

l= [tuple(map(int,input().split())) for _ in range(E)]


l.sort(key=lambda x:(x[2]))

ans = 0

parent = [i for i in range(V+1)]

def union(a,b):
    ra =  find(a)
    rb = find(b)
    if ra > rb:
        parent[ra] = rb
    else:
        parent[rb] = ra


def find(n):
    if n ==parent[n]: 
        return n
    parent[n] = find(parent[n])
    return parent[n]

for i in l:
    if find(i[0]) != find(i[1]):
        union(i[0],i[1])
        ans += i[2]


print(ans)