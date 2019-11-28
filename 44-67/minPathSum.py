
class Solution:
    def minPathSum(self, grid):

        n, m = len(grid), len(grid[0])
        # dp = [0]*m
        for i in range(1, m):
            grid[0][i] += grid[0][i - 1]
        for i in range(1, n):
            for j in range(m):
                # if i == 0:
                #     dp[j] = grid[i][j] + dp[j - 1]
                if j == 0:
                    # dp[j] += grid[i][j]
                    grid[i][j] += grid[i - 1][j]
                else:
                    # dp[j] = grid[i][j] + min(dp[j - 1], dp[j])
                    grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

        return grid[-1][-1]

    
def main():
    grid = [
[1, 2, 3]
]
    a = Solution()
    print(a.minPathSum(grid))


if __name__ == '__main__':
    main()
