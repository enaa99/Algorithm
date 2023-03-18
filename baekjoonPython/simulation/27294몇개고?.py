import sys

input = sys.stdin.readline


# 시간 11시 이하 아침, 12~16 점심, else 저녁

# 술의 유무 1 술있게, 0 없게

T,S = map(int,input().split())

if S:
    print(280)
else:
    if  12<=T<=16:
        print(320)
    else:
        print(280)