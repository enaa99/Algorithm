from typing import MutableSequence

def heap_sort(a: MutableSequence)->None:
    def down_heap(a:MutableSequence, left: int, right:int)->None:
        temp = a[left]          # 루트
        
        parent = left
        while parent < (right + 1) // 2:
            lchild =parent * 2 + 1          # 왼쪽 자식
            rchild = lchild + 1             # 오른쪽 자식
            child = rchild if rchild <= right and a[rchild] > a[lchild] else lchild # 큰 값을 선택
            if temp >= a[child]:
                break
            a[parent] = a[child]
            parent = child
        a[parent] = temp
    
    n = len(a)
    
    for i in range((n-1)//2,-1,-1):     #a[i]~a[n-1]을 힙으로 만들기
        down_heap(a,i,n-1)
        
    for i in range(n-1,0,-1):
        a[0],a[i] = a[i],a[0]           # 최대값인 a[0]과 마지막 원소를 교환
        down_heap(a,0,i-1)             # a[0]~a[i-1]을 힙으로 만들기
        
if __name__ == '__main__':
    print('힙 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None]*num                  # 원소 수가 num인 배열을 생성
    
    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))
            
    heap_sort(x)                    # 배열 x를 힙 정렬
        
    print('오름차순으로 정렬했습니다.')
        
    for i in range(num):
        print(f'x[{i}] = {x[i]}')