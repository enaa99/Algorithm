def solution(numlist, n):
    
    numlist.sort(reverse=True)
    
    numlist.sort(key = lambda x:abs(x-n))

    
    return numlist







def solution(k,n,a,b,A):
    
    isUsed = [0]*(b-a+1)
    
    for i in range(len(A)):
        
        if A[i] <= a:
            while A[i] <= b:
                if A[i] >= a and not isUsed[A[i]-a]:
                    isUsed[A[i]-a] = 1
                    break
                A[i] += k
        elif A[i] >= b:
            while A[i] >= a:
                if A[i] <=b and not isUsed[A[i]-b]:
                    isUsed[A[i]-a] = 1
                    break
                A[i] -= k
                
	