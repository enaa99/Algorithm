import sys

input = sys.stdin.readline

strings = ['a','e','i','o','u','A','E','I','O','U']


while True:
    S = input().rstrip()
    
    if S == '#': break
    cnt = 0
    for i in S:
        if i in strings:
            cnt +=1
    print(cnt)