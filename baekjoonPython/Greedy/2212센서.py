import sys

input = sys.stdin.readline

# 센서의 개수
N = int(input())


# 집중국의 개수
K = int(input())

sensors = list(map(int,input().split()))

sensors.sort()

tmp = []
for i in range(1,N):
    tmp.append(sensors[i]-sensors[i-1])

tmp.sort()
ans = 0
for i in range(N-K):
    ans += tmp[i]


print(ans)