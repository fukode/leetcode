class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        if obstacleGrid[0][0] or obstacleGrid[-1][-1]: return 0
        # dp = [[0] * len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]
        # i = 0
        # while i < len(obstacleGrid[0]) and not obstacleGrid[0][i]: i += 1
        # dp[0][0: i] = [1] * i
        # for i in range(1, len(obstacleGrid)):
        #     if obstacleGrid[i][0]:
        #         break
        #     else:
        #         dp[i][0] = 1
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        dp = [1] + [0] * m
        for i in range(n):
            for j in range(m):
                dp[j] = 0 if obstacleGrid[i][j] else dp[j] + dp[j - 1]

        return dp[-2]


def main():
    obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
    a = Solution()
    print(a.uniquePathsWithObstacles(obstacleGrid))


if __name__ == '__main__':
    main()
