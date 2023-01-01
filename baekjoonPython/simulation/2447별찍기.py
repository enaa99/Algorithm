import sys

input = sys.stdin.readline

N = int(input())

def start(k):
    if k == 3:
        return ['***','* *','***']
    
    candy = []
    
    star = start(k//3)
    
    for i in star:
        candy.append(i*3)
    
    for i in star:
        candy.append(i+" "*(k//3)+i)
    
    for i in star:
        candy.append(i*3)
    return candy

print("\n".join(start(N)))