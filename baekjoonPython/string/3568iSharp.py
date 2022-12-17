import sys

tmp = input().rstrip()
l = tmp.split(' ')

first = l[0]

for i in range(1,len(l)):
    # ','와 ';' 제거
    l[i] = l[i].replace(",", '').replace(";", '')

    # 기본 변수형 출력
    print(first, end='')

    for j in range(len(l[i]) - 1, 0, -1):
        if not l[i][j].isalpha():
            if l[i][j] == ']':
                print('[', end='')
            elif l[i][j] == '[':
                print(']', end='')
            else:
                print(l[i][j], end='')

    print(' ', end='')

    for k in range(len(l[i])):
        if l[i][k].isalpha():
            print(l[i][k], end='')

    print(';')