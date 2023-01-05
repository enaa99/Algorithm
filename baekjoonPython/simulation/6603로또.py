import sys
from itertools import combinations,permutations,product

input = sys.stdin.readline



while True:
    A = list(map(int,input().split()))
    
    if len(A) == 1:
        exit(0)
        
    A.pop(0)
    
    nums = list(combinations(A,6))
    
    for i in nums:
        for j in i:
            print(j,end=' ')
        print()
    print()