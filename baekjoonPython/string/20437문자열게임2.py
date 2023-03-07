import sys
from collections import Counter

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    
    W = list(input().rstrip())
    N = int(input())
    
    dic = Counter(W)
    
    
    tmp = []
    for i in range(len(W)):
        cnt = N -1
        if dic[W[i]] >= N:
            dic[W[i]] -= 1
            for j in range(i+1,len(W)):
                if W[j] == W[i]: 
                    cnt -=1
                
                    if cnt == 0:
                        if i == 0:
                            tmp.append(j)
                        else:
                            tmp.append(j-i+1)
                        break
    if tmp:
        print(min(tmp),end = ' ')
        print(max(tmp))
    else:
        print(-1)