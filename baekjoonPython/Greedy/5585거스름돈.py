import sys

input = sys.stdin.readline

N = int(input())

moneys = [500,100,50,10,5,1]
k = 0

charge = 1000-N

for money in moneys:
    check = charge//money
    
    if check > 0:
        k += check
        charge = charge-check*money
    
    if charge <= 0:
        break

print(k)