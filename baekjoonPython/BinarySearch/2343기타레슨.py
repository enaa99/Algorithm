import sys

input = sys.stdin.readline

N,M = map(int,input().split())

graph = list(map(int,input().split()))

def binary_search():
    l = max(graph)-1
    r = sum(graph)+1

    while l +1 < r:
        mid = (l+r)//2
        tmp = 0
        cnt = 1
        
        for i in graph:
            if tmp+i <= mid:
                tmp += i
            else:
                cnt +=1
                tmp = i
            if cnt > M:
                break
        if cnt > M:
            l = mid
        else:
            r = mid
    return r

print(binary_search())