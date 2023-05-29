def solution(n):
    answer = 0
    
    arr = [-1]*n
    
    def check(x):
        for i in range(x):
            if arr[x] == arr[i] or abs(arr[x]-arr[i]) == abs(x-i):
                return False
        return True
    
    
    
    def DFS(depth):
        nonlocal answer
        if depth == n:
            answer +=1
            return
        
        for i in range(n):
            arr[depth] = i
            if check(depth):
                DFS(depth+1)
    DFS(0)
    
    return answer

solution(12)