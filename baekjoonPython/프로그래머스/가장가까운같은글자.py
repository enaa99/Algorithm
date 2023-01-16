def solutioin(s):
    
    save_dic = {}
    ans = []
    for i in range(len(s)):
        if save_dic.get(s[i],True) :
            ans.append(-1)
        else:
            ans.append(i-save_dic[s[i]])
        save_dic[s[i]] = i
    
    #dp = [-1]*len(s)
    
   # for i in range(1,len(s)):
   #    for j in range(i-1,-1,-1):
   #        if s[i] == s[j]:
   #           dp[i] = i-j
   #           break

    
    return ans
    # dp = [-1]*len(s)
    
    # for i in range(1,len(s)):
    #     for j in range(i-1,-1,-1):
    #         if s[i] == s[j]:
    #             dp[i] = i-j
    #             break
    
    
    return dp


solutioin("banana")