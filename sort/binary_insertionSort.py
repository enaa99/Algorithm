from typing import MutableSequence

# 이진 삽입 정렬
def binary_insertion_sort(a):
    for i in range(len(a)):
        temp = a[i]
        left = 0
        right = i-1
        
        while True:
            mid = (left+right)//2
            if(a[mid]==a[i]):
                break
            elif temp > a[mid]:
                left = mid +1
            else:
                right = mid -1
            if left>right:
                break
        pd = mid +1 if left<=right else right+1
        
        for j in range(i,pd,-1):
            a[j] = a[j-1]
        a[pd] = temp
        
if __name__ == "__main__":
    print('이진 삽입 정렬을 수행합니다.')
    
    num = int(input("원소 수를 입력하세요.: "))
    x =[None]*num
    
    for i in range(num):
        x[i] = int(input(f'x[{i}]'))
        
    binary_insertion_sort(x)
    
    print("오름차순으로 정렬했습니다.")
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
        
        

