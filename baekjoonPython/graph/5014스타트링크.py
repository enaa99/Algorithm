import sys
from collections import deque
input = sys.stdin.readline

# 총 F 층
# 스타트링크 G
# 현재위치 S
# U층위 D층아래
# 갈 수 없다면 use the stairs


# F S G U D

F,S,G,U,D = map(int,input().split())

# 최소값
isVisited = [0]*(F+1)
q = deque()
answer = 0

if S == G:
    print(0)
    exit(0)

q.append([S,answer])
while q:
    v,cnt = q.popleft()
    
    if v > F or v<1 or isVisited[v]: continue
    
    if v == G: 
        print(cnt)
        exit(0)
    isVisited[v] = 1
    q.append([v+U,cnt+1])
    q.append([v-D,cnt+1])

print("use the stairs")