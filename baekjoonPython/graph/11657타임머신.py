import sys

input = sys.stdin.readline

# bellman-ford

V,E = map(int,input().split())


edges = []

distance = [sys.maxsize]*(V+1)


#모든간선검사해야된다
# v-1번째에 
for _ in range(E):
    a,b,c = map(int,input().split())
    edges.append((a,b,c))



def bellman_ford(start):
    distance[start] = 0
    
    for i in range(V):
        for cur,next,edge in edges:
            
            if distance[cur] != sys.maxsize and distance[next] > distance[cur]+edge:
                distance[next] = distance[cur]+edge
                if i == V-1:
                    return True
    
    return False

if bellman_ford(1):
    print(-1)
    exit(0)
    
for i in range(2,V+1):
    if distance[i] == sys.maxsize:
        print(-1)
    else:
        print(distance[i])