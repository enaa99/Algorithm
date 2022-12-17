import sys
input = sys.stdin.readline

for _ in range(int(input())): # 테스트 케이스
    l = []
    cnt = 1
    n = int(input())
    for __ in range(n): # 면접 지원자 수
        a,b = map(int,input().split()) # a 서류심사 성적 / b 면접 성적
        l.append((a,b))
    l.sort(key=lambda x:x[0])
    tmp = l[0][1]
    for i in range(1,n):
        if tmp > l[i][1]:
            tmp = l[i][1]
            cnt +=1
    print(cnt)