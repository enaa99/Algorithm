from typing import MutableSequence
import bisect
# 삽입 정렬

def insertion_sort(a)->None:
    for i in range(1,len(a)):
        j = i
        temp = a[i]
        while j>0 and temp < a[j-1]:
            a[j]=a[j-1]
            j -=1
        a[j] = temp

def insert(a):
    for i in range(1,len(a)):
        j = i
        temp = a[i]
        while j>0 and temp <a[j-1]:
            a[j] = a[j-1]
            j -= 1
            a[j] = temp


if __name__ == '__main__':
    print('단순 삽입 정렬 수행')
    num = int(input('원소 수를 입력하세요.: '))
    x =[None]*num
    
    for i in range(num):
        x[i] = int(input(f'x[{i}]'))
        
    insertion_sort(x)
    
    print('오름차순으로 정렬')
    for i in range(num):
        print(f'x[{i}]={x[i]}')
    
    
#-----------------------------
def binary_insert(a)->None:
    for i in range(1,len(a)):
        bisect.insort(a,a.pop(i),0,i)