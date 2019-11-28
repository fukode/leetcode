class Solution:
    def minDistance(self, word1, word2):
        n, m = len(word1), len(word2)
        dp = [[0] + [i + 1 for i in range(m)]] + [[i] + [0] * m for i in range(1, n + 1)]

        for i in range(n):
            for j in range(m):
                if word1[i] == word2[j]:
                    dp[i + 1][j + 1] = dp[i][j]
                else:
                    dp[i + 1][j + 1] = min(dp[i][j + 1], dp[i + 1][j], dp[i][j]) + 1
        return dp[-1][-1]

    
def main():
    word1 = "horse"

    word2 = "ros"
    a = Solution()
    print(a.minDistance(word1, word2))


if __name__ == '__main__':
    main()
