import sys

input = sys.stdin.readline

player = 1
time = 12

plus = 1

N = int(input())

for _ in range(N):
    a,b = map(str,input().split())
    
    if a == 'HOURGLASS':
        time += plus
        
        if time <= 0:
            time = 12 + time
        elif time > 12:
            time = time - 12
        if time == int(b):
            print(time,'NO')
        else:
            plus *= -1
            
            print(time,'NO')
        
        
    else:
        time += plus
        if time <= 0:
            time = 12 + time
        elif time > 12:
            time = time - 12
        
        if time == int(b):
            print(time,'YES')
        else:
            print(time,'NO')
