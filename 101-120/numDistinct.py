class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0] * (len(s) + 1) for _ in range(len(t) + 1)]
        for i in range(len(s) + 1):
            dp[0][i] = 1

        for i in range(len(t)):
            for j in range(len(s)):
                dp[i + 1][j + 1] = dp[i][j] + dp[i + 1][j] if t[i] == s[j] else dp[i + 1][j]
        return dp[-1][-1]