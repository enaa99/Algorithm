import sys

input = sys.stdin.readline

# 소문자 대문자 숫자 공백

while True:
    arr =[0]*4
    try:
        k = list(input().rstrip('\n'))
        if not k: break
        for i in k:
            
            if i.islower():
                arr[0] += 1
            elif i.isupper():
                arr[1] += 1
            elif i.isdecimal():
                arr[2] += 1
            else:
                arr[3] += 1
        print(*arr)
    except:
        break
