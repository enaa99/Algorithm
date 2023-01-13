#from itertools import permutations
def solution(n, k):
    
    #people = [i for i in range(1,n+1)]
    
    #answer = list(permutations(people,n))
    
    #ans = list(answer[k-1])
        
    isUsed = [0]*(n+1)
    ans = []
    def dfs(arr,depth):
        if len(ans) == k : return
        if depth == n:
            ans.append(arr[:])
            
            return
        for i in range(1,n+1):
            if not isUsed[i]:
                arr[depth] = i
                isUsed[i] = 1
                dfs(arr,depth+1)
                isUsed[i] = 0
    
    dfs([0]*n,0)
    
    
    return ans[-1]

solution(3,5)