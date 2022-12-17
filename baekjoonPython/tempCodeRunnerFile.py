import sys

l =[]
for _ in range(int(sys.stdin.readline())):
    l.append(int(sys.stdin.readline()))
    

# Library 사용
# l.sort()
# print(*l,sep='\n')

# 2. qsort()구현
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

qsort(l,0,len(l)-1)
print(*l,sep='\n')
