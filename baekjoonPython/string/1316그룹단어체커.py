import sys

input = sys.stdin.readline

N = int(input())
answer = 0
for _ in range(N):
    K = input().rstrip()
    q =[]
    flag = 0
    for i in range(len(K)):
        if not q:
            q.append(K[i])
        else:
            if q[-1] == K[i]: continue
            
            else:
                if K[i] in q: 
                    flag = 1
                    break
                else:
                    q.append(K[i])
    if not flag:
        answer +=1

print(answer)