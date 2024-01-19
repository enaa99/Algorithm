import sys
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        M,N = len(matrix), len(matrix)

        dp = [[sys.maxsize]*M for _ in range(N)]

        for i in range(M):
            dp[0][i] = matrix[0][i]

        if M == 1:
            return min(matrix[0])
        

        for i in range(1,M):
            for j in range(N):
                if j == 0:
                    dp[i][j] = min(dp[i][j], matrix[i][j] + min(dp[i-1][j], dp[i-1][j+1]))
                elif j == M-1:
                    dp[i][j] = min(dp[i][j], matrix[i][j] + min(dp[i-1][j], dp[i-1][j-1]))
                else:
                    dp[i][j] = min(dp[i][j], matrix[i][j] + min(dp[i-1][j], dp[i-1][j-1], dp[i-1][j+1]))


        return min(dp[M-1])
