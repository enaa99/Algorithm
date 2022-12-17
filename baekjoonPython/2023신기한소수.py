import sys

input = sys.stdin.readline


N = int(input())

def Prime(k):
    while k>0:
        k //= 10
        for i in range(2,int(k**0.5)+1):
            if k%i == 0:
                return False
            # if isCheck[i]: return True
    return True
    
#10**(N-1)
passing = [1,4,6,8,9]
passing2 = [0,2,4,6,8]
j = 10**(N-1)
while j<10**N:
    isInclude = False
    tiempo = j//10**(N-1)
    if tiempo in passing :
        j += 10**(N-1)
        continue
    tmp = str(j)
    for qq in range(1,len(tmp)):
        if int(tmp[qq]) in passing2:
            isInclude = True
            j += 10**(N-qq-1)
            break
    if isInclude : continue
    
    check = False
    for w in range(2,int(j**0.5)+1):
        if j%w == 0:
            check = True
            break
    if not check:
        if Prime(j):
            print(j)
    j+=1