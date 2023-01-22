import sys
from collections import defaultdict

input = sys.stdin.readline


N,M = map(int,input().split())



n_dict = defaultdict(int)

for _ in range(N):
    n_dict[input().rstrip()]


for _ in range(M):
    k = input().rstrip()
    
    if k in n_dict:
        n_dict[k] += 1

sum = 0
for i in n_dict.values():
    sum += i

print(sum)


