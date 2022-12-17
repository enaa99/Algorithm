import sys

l =[]
for _ in range(int(sys.stdin.readline())):
    l.append(int(sys.stdin.readline()))
    

# Library 사용
# l.sort()
# print(*l,sep='\n')

# 2. qsort()구현 why?..
def qsort(a,left,right):
    l = left
    r = right
    pivot = a[(left+right)//2]
    
    while l <= r:
        while a[l] < pivot : l += 1
        while a[r] > pivot : r -= 1
    
        if l<=r:
            a[l],a[r] = a[r],a[l]
            l += 1
            r -= 1
    if left<r : qsort(a,left,r)
    if l <right : qsort(a,l,right)

# 3. merge_sort() 구현
def merge_sort(a):
    def _merge_sort(a,left,right):
        if left < right:
            mid =(left+right)//2
            
            _merge_sort(a,left,mid)
            _merge_sort(a,mid+1,right)
            
            p = j = 0
            l = k = left
            
            while l<= mid:
                buff[p] = a[l]
                p += 1
                l += 1
            
            while l<= right and j<p:
                if buff[j] <= a[l]:
                    a[k] = buff[j]
                    j += 1
                else :
                    a[k] = a[l]
                    l += 1
                k += 1
            while j < p:
                a[k] = buff[j]
                k += 1
                j += 1
            
    n = len(a)
    buff = [None]*n
    _merge_sort(a,0,n-1)
    del buff
    
merge_sort(l)
print(*l,sep='\n')