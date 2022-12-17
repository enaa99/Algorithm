import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline


# a[i] == 1 -> i는 실내
# a[i] == 0 -> i는 실외

# 시작 & 끝점  => 실내 반드시
# 서로 다른 산책 경로 수 출력


N =int(input())

place = [int(i) for i in input().strip()]

l = [[]for _ in range(N+1)]
isUsed =[False]*(N+1)


ans = 0
tmp = 0
def dfs(cnt):
    global tmp
    isUsed[cnt] = True
    for i in l[cnt]:
            if  place[i-1] == 1: tmp += 1
            elif place[i-1] ==0 and not isUsed[i]: dfs(i)
def dfs2(cnt):
    global tmp
    isUsed[cnt] = True
    for i in l[cnt]:
            if not isUsed[i]:
                if place[i-1] ==0:
                    dfs(i)
                else:
                    tmp+=1
            # if  place[i-1] == 1: tmp += 1
            # elif place[i-1] ==0 and not isUsed[i]: dfs(i)

for _ in range(1,N):
    a,b = map(int,input().split())
    l[a].append(b)
    l[b].append(a)
    if place[a-1] == 1 and place[b-1] == 1  :
        ans +=2

for i in range(1,N+1):
    tmp = 0
    if place[i-1] == 0 and not isUsed[i]: 
        dfs(i)
    ans += tmp*(tmp-1)
print(ans)