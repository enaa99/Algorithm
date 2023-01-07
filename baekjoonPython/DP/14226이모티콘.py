import sys
from collections import deque

input = sys.stdin.readline



########################
# S = int(input())
# DP 풀이

# dp = [sys.maxsize]*(1002)

# dp[1] = 0
# for i in range(1,1001):
#     for j in range(2,1001):
#         if i*j < 1001:
#             dp[j*i] = min(dp[j*i],dp[i]+j)
    
#     for j in range(1000,1,-1):
#         dp[j] = min(dp[j],dp[j+1]+1)

# print(dp[S])



#######################
# BFS 풀이

n = int(input())
dist = [[-1]* (n+1) for _ in range(n+1)]
q = deque()
q.append((1,0))  # 화면 이모티콘 개수, 클립보드 이모티콘 개수
dist[1][0] = 0
while q:
    s,c = q.popleft()
    if dist[s][s] == -1: #복사
        dist[s][s] = dist[s][c] + 1
        q.append((s,s))
    if s+c <= n and dist[s+c][c] == -1: # 붙여넣기
        dist[s+c][c] = dist[s][c] + 1
        q.append((s+c, c))
    if s-1 >= 0 and dist[s-1][c] == -1: # 지우기
        dist[s-1][c] = dist[s][c] + 1
        q.append((s-1, c))
answer = sys.maxsize
for i in range(n+1):
    if dist[n][i] != -1:
        if answer > dist[n][i]:
            answer = dist[n][i]
print(answer)