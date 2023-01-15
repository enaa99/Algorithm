import sys

input = sys.stdin.readline

word = input().rstrip()

# 65
arr = [0]*26

cnt = 3
for i in range(3,26,3):
    if cnt == 8:
        arr[i-3] = arr[i-2] = arr[i-1] = arr[i] = cnt
    elif cnt ==10:
        arr[i-2] = arr[i-1] = arr[i] = arr[i+1] = cnt
    elif cnt >8:
        arr[i-2] = arr[i-1] = arr[i] = cnt
    else:
        arr[i-3] = arr[i-2] = arr[i-1] = cnt
    cnt +=1 

ans = 0
for i in word:
    ans +=arr[ord(i)-65]

print(ans)