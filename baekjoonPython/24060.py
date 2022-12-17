import sys
from tabnanny import check
sys.setrecursionlimit(10**9)

n, k = map(int,sys.stdin.readline().split())
cnt = 0
isCheck = False

def merge_sort(arr):
    def sort(low, high):
        global isCheck
        if isCheck:return
        if high - low <= 1:
            return
        mid = (low + high+1)// 2
        sort(low, mid)
        sort(mid, high)
        merge(low, mid, high)

    def merge(low, mid, high):
        global isCheck
        global cnt
        if isCheck:return
        temp = []
        l, h = low, mid
        while l < mid and h < high:
            if arr[l] <= arr[h]:
                temp.append(arr[l])
                l += 1
            else:
                temp.append(arr[h])
                h += 1

        while l < mid:
            temp.append(arr[l])
            l += 1
        while h < high:
            temp.append(arr[h])
            h += 1

        for i in range(low, high):
            arr[i] = temp[i - low]
            cnt += 1
            if cnt == k:
                print(arr[i])
                isCheck = True
                break
        
    return sort(0, len(arr))

l = list(map(int,sys.stdin.readline().split()))

merge_sort(l)

if not isCheck: print(-1)