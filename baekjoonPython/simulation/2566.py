import sys

input = sys.stdin.readline


answer = [-1,0,0]
for i in range(9):
    
    l = list(map(int,input().split()))
    
    max_v = max(l)
    k = [max_v,i+1,l.index(max_v)+1]
    
    if answer[0] < k[0]:
        answer[0],answer[1],answer[2] = k[0],k[1],k[2]
    
print(answer[0])
print(answer[1],answer[2])