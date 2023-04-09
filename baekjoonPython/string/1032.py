import sys

input = sys.stdin.readline

T = int(input())
k = []
for _ in range(T):

    if not k :
        k = list(input().rstrip())
    else:
        cmp = input().rstrip()
        
        for i in range(len(cmp)):
            if k[i] != cmp[i]:
                k[i] = '?'
print(''.join(k))