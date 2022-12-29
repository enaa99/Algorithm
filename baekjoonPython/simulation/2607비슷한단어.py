import sys

input = sys.stdin.readline

N = int(input())


first = input().rstrip()

f_len = len(first)

ans = 0

def checks(tmp,cnt):
    for s in first:
        if s in tmp:
            k = tmp.index(s)
            tmp.pop(k)
            cnt += 1
    return cnt


for _ in range(N-1):
    check = list(input().rstrip())
    cnt = 0
    c_len =len(check)
    
    if c_len > f_len +1 or c_len < f_len -1 : continue
    
    cnt = checks(check,cnt)

    if c_len <= f_len and f_len-1 <=cnt:
        ans += 1
    else:
        if f_len -1 < cnt <= f_len +1:
            ans +=1
print(ans)