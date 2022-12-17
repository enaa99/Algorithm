from heapq import merge
from typing import MutableSequence



# 병합 정렬
def merge_sort(arr):
    def sort(low, high):
        if high - low < 2:
            return
        mid = (low + high) // 2
        sort(low, mid)
        sort(mid, high)
        merge(low, mid, high)

    def merge(low, mid, high):
        temp = []
        l, h = low, mid

        while l < mid and h < high:
            if arr[l] < arr[h]:
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

    return sort(0, len(arr))
if __name__ =='__main__':
    print('병합 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None]*num                  # 원소 수가 num인 배열을 생성
    
    for l in range(num):
        x[l] = int(input(f'x[{l}]: '))
    
    merge_sort(x)                   # 배열 x를 병합 정렬
    
    print('오름차순으로 정렬했습니다.')
    
    for l in range(num):
        print(f'x[{l}] = {x[l]}')