import sys
from collections import defaultdict
input = sys.stdin.readline

a,b = map(int,input().split())


a_dic = defaultdict(int)
answer = []

for i in range(a):
    a_dic[input().rstrip()] = 1


for j in range(b):
    k = input().rstrip()
    if a_dic[k]:
        answer.append(k)
answer.sort()
print(len(answer))
print(*answer, sep='\n')


