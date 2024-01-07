def qsort(a, left, right):
    pl = left
    pr = right
    
    mid = a[(right + left)//2]
    
    while pl <= pr:
        while a[pl] < mid : pl +=1
        while a[pr] > mid : pr -=1
        
        if pl<=pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl +=1
            pr -=1
            
            if pl < right: qsort(a,pl,right)
            if pr > left: qsort(a, left, pr)