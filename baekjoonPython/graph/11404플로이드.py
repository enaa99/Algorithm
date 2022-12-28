import sys

input = sys.stdin.readline

N = int(input())
M = int(input())

bus = [[sys.maxsize]*(N+1) for _ in range(N+1)]


for i in range(M):
    a,b,c = map(int,input().split())
    bus[a][b] = min(bus[a][b],c)
    
# for i in range(1,N+1):
#     for j in range(1,N+1):
#         if i== j:
#             bus[i][j] =0

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            bus[i][j] = min(bus[i][j],bus[i][k]+bus[k][j])

for i in range(1,N+1):
    for j in range(1,N+1):
        if i == j or bus[i][j] == sys.maxsize:
            bus[i][j] = 0
        
        print(bus[i][j],end =" ")
    print()