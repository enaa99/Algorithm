def solution(n):
    answer = 0
    
    arr = [0]*(n+4)
    
    arr[0],arr[1],arr[2],arr[3] = 0,1,1,2
    
    for i in range(4,n+1):
        arr[i] = (arr[i-2]+arr[i-1])%1234567
    
    
    return arr[n]