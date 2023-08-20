from collections import defaultdict
import sys
def solution(sales, links):
    
    # 모든 팀은 최소 1명 이상 워크숍 참석
    # 워크숍에 참석하는 직원들의 하루평균 매출액의 합이 최소
    
    dp = [[0,0]] + [[0, sale] for sale in sales]
    
    
    team_dict = defaultdict(list)
    for a,b in links:
        team_dict[a].append(b)
    
    
    def dfs(node):
        if not team_dict[node]:
            return
        
        cnt, zero_cnt, min_val, min_diff = 0,0,0,sys.maxsize
        
        for leaf in team_dict[node]:
            dfs(leaf)
            
            min_val += min(dp[leaf])
            cnt += 1
            if dp[leaf][0] < dp[leaf][1]:
                zero_cnt +=1 
                min_diff = min(min_diff,dp[leaf][1] - dp[leaf][0])
        
        dp[node][1] += min_val
        dp[node][0] += min_val + min_diff if cnt == zero_cnt else min_val    
    
    dfs(1)
    
    return min(dp[1][0],dp[1][1])

solution([14, 17, 15, 18, 19, 14, 13, 16, 28, 17],
         [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]])