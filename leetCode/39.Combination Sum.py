def combinationSum(candidates, target) :
        answer = []
        def dfs(n,k):
            if sum(n) > k:
                return
            elif sum(n) == k:
                answer.append(arr)
                return

            for i in candidates:
                arr = n.copy()
                arr.append(i)
                dfs(arr,k)
        return answer
    
