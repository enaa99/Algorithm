def solutioin(s):
    
    dp = [-1]*len(s)
    
    for i in range(1,len(s)):
        for j in range(i-1,-1,-1):
            if s[i] == s[j]:
                dp[i] = i-j
                break
    
    
    return dp