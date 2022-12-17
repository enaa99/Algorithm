import sys

input = sys.stdin.readline
N = int(input())
W = [0] * N
for i in range(N):
    W[i] = list(map(int, input().split()))
M = [[0] * (1 << N) for i in range(N)]

def dfs(node, visited):
    # 모든 도시를 방문 했다면
    if visited == (1 << N) - 1:
        return W[node][0] if W[node][0] else sys.maxsize
    # 최소 비용이 이미 계산 되어있다면
    if M[node][visited] != 0:
        return M[node][visited]
    cost = sys.maxsize
    for i in range(1, N):
        # 해당 도시로 가는 경로가 없다면 skip
        if not W[node][i] or visited & (1 << i):
            continue

        cost = min(cost, W[node][i] + dfs(i, visited | (1 << i)))
    M[node][visited] = cost
    return cost

print(dfs(0, 1))