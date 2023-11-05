class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # () / (()) ()() / 
        arr = []
        def dfs(l,r,s):
            if len(s) == n*2:
                arr.append(s)
                return
            
            if l < n:
                dfs(l+1,r,s+'(')
            if r < l:
                dfs(l,r+1,s+')')
        
        dfs(1,0,'(')
        return arr
