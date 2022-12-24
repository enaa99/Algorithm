import sys

input = sys.stdin.readline

N = int(input())

graph = list(map(int,input().split()))

dp =[1]*N


for i in range(len(graph)):
    for j in range(i,-1,-1):
        if graph[i] > graph[j] and dp[i] <= dp[j]:
            dp[i] = dp[j]+1


ans = max(dp)
print(ans)

order = ans
l =[] 
for i in range(len(graph)-1,-1,-1):
    if dp[i] == order:
        l.append(graph[i])
        order -= 1
# l = []
# for i in range(ans,0,-1):
#     for j in range(len(dp)-1,-1,-1):
#         if dp[j] == i:
#             l.append(graph[j])
#             break

l.reverse()
print(*l)