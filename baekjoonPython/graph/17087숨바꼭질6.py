import sys

input = sys.stdin.readline

N,S = map(int,input().split())

graph = list(map(int,input().split()))

def gcd(x,y):
    
    if y ==0: return x
    
    return gcd(y, x % y)

if len(graph) == 1:
    print(abs(graph[0]-S))
    exit(0)


for i in range(len(graph)):
    graph[i] -= S
    
    graph[i] = graph[i] if graph[i] >=0 else graph[i]*-1

graph.sort()
check = graph[0]
for i in range(1,len(graph)):
    check = gcd(graph[i],check)
print(check)
