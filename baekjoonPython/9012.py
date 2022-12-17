import sys

input = sys.stdin.readline


for _ in range(int(input())):
    k = [0]*2
    isCheck = False
    for i in input():
        if i == '(':
            k[0] +=1
        elif i == ')':
            if k[0] > k[1]:
                k[1] +=1
            else:
                isCheck= True
                break
    if k[0] == k[1] and not isCheck: print('YES')
    else : print('NO')