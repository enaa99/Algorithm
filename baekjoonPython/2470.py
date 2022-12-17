import sys

input = sys.stdin.readline

n = int(input())

o = sorted(list(map(int,input().split())))

o.sort()

def check(m):
    return m >= 0
ans =[0,0]

def binary_search(left,right,low,high):
    l = left
    r = right
    s = low
    e = high
    answer = sys.maxsize
    
    while l < r:
        tmp = l +r
        if abs(answer) > abs(tmp):
            answer = tmp
            ans[0],ans[1] = o[s],o[e]
            if tmp == 0 :break

        if check(tmp):
            e -= 1
            r = o[e]
            
        else :
            s +=1
            l = o[s]

binary_search(o[0],o[-1],0,(len(o)-1))
ans.sort()
print(*ans)