import sys
from collections import deque

input = sys.stdin.readline

S = input().strip()

T = input().strip()

# 1. 문자열의 뒤에 A를 추가
# 2. 문자열의 뒤에 B를 추가하고 문자열 뒤집는다

len_s = len(S)
def BFS():
    q = deque()
    q.append(T)
    
    while q:
        k = q.popleft()
        
        if len_s > len(k) : continue
        
        if S == k:
            return 1
        
        if k[-1] == 'A':
            q.append(k[:-1])
        if k[0] == 'B':
            k = k[::-1]
            q.append(k[:-1])
        
            
    return 0

print(BFS())