import sys

# n = int(sys.stdin.readline())
# l =[]
# for i in range(n):
#     l.append(int(sys.stdin.readline()))


# 1. insertion_sort (메모리 초과)
def insertion_sort(a):
    for i in range(len(a)):
        temp = a[i]
        j = i
        while j>0 and temp < a[j-1]:
            a[j] = a[j-1]
            j -= 1
        a[j] = temp



# 2. binary_insertion_sort (메모리 초과)
def binary_insertion_sort(a):
    for i in range(len(a)):
        temp = a[i]
        left = 0
        right = i-1
        while True:
            mid = (left+right)//2
            if(a[mid] == a[i]):
                break
            elif temp > a[mid]:
                left = mid+1
            else:
                right = mid - 1
            if left > right:
                break
        idx = mid +1 if left <= right else right+1
        
        for j in range(i,idx,-1):
            a[j] = a[j-1]
        a[idx] = temp
        
# 3. quick_sort
def qsort(a,left,right):
    pl = left
    pr = right
    pivot = a[left]
    
    while pl<=pr:
        while a[pl] < pivot: 
            pl +=1
        while a[pr] > pivot: 
            pr -=1
        if pl<=pr:
            a[pl],a[pr] = a[pr],a[pl]
            pl +=1
            pr -=1
    if left<pr:qsort(a,left,pr)
    if right>pl:qsort(a,pl,right)

def quick_sort(n)->None:
    qsort(n,0,len(n)-1)

# 4. Counting 정렬
l =[0]*10001
for _ in range(1,int(sys.stdin.readline())+1):
    l[int(sys.stdin.readline())] +=1
    

for i in range(1,10001):
    for j in range(l[i]):
        print(i)

# binary_insertion_sort(l)
# insertion_sort(l)
# quick_sort(l)
# print(l)