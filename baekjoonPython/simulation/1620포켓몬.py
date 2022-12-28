import sys

input = sys.stdin.readline

N,M = map(int,input().split())

poke = {}

for i in range(N):
    name = input().strip()
    poke[name] = i+1
    poke[f"{i+1}"] = name

pokelist = list(poke.keys())

for i in range(M):
    check = input().strip()
    print(poke[check])

# for i in range(M):
#     x = input().rstrip()
#     try:
#         poke[x]
#     except:
#         pokelist[int(x)-1]

# print(pokelist)