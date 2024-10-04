def get_max_profit(pnl, k):
    n = len(pnl)
    dp = [0] * n
    dp[0] = pnl[0]  # 첫 번째 값은 자기 자신이 최대
    max_sum = dp[0]  # 전체 최대합

    for i in range(1, n):
        current_sum = pnl[i]
        dp[i] = current_sum  # i번째 요소 자체로 시작하는 경우
        
        # i번째 요소에서 최대 k길이 이하의 부분 배열 고려
        for j in range(1, k):
            if i < j:
                break
            current_sum += pnl[i - j]
            dp[i] = max(dp[i], current_sum)
        
        max_sum = max(max_sum, dp[i])  # 전체 최대값 갱신

    return max_sum


print(get_max_profit([4, 3, -2, 9, -4, 2, 7, 6], 6))
print(sum([4, 3, -2, 9, -4, 2, 7, 6]))
