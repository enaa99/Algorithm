import sys

brown = 50
yellow = 22
check = brown+yellow
# tmp = a+b
tmp = brown//2 + 2
answer = []
a = b = tmp//2
if a+b != tmp: a+=1 
while b >=3:
    while(check%a != 0): a += 1
    while(a+b != tmp): b -= 1
    if a+b == tmp and (a-2)*(b-2) == yellow:
        answer.append(a)
        answer.append(b)
        break
    a += 1
    b -= 1
        
print(*answer)