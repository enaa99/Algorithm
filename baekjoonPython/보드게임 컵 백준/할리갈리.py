import sys

input = sys.stdin.readline

N = int(input())

fruits = {'STRAWBERRY':0,'BANANA':0,'LIME':0,'PLUM':0}

for _ in range(N):
    a,b = map(str,input().split())

    fruits[f'{a}'] += int(b)

for i in fruits.keys():
    if fruits[i] == 5:
        print('YES')
        exit(0)
print('NO')