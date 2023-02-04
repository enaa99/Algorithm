import sys
from collections import defaultdict
from collections import deque
input = sys.stdin.readline

# N 월급 변화, 조사 쿼리 수 M

# p a x -> a의 모든 부하의 월급 x만큼 증가
# u a -> a의 월급 출력

N,M = map(int,input().split())

cmd = [[]for _ in range(N+1)]

budget = defaultdict(int)

for i in range(N):
    k = list(map(int,input().split()))
    
    if i == 0:
        budget[1] = k[0]
    
    if i != 0:
        cmd[k[1]].append(i+1)
        budget[i+1] = k[0]

def BFS(cnt,k):
    q = deque()
    q.append(cnt)
    
    while q:
        v = q.popleft()
        for i in cmd[v]:
            budget[i] += k
            q.append(i)



for _ in range(M):
    query = list(map(str,input().split()))
    if query[0] == 'p':
        BFS(int(query[1]),int(query[2]))
    else:
        print(budget[int(query[1])])