
class Solution:
    def uniquePaths(self, m, n):
        dp = [1] * m
        for i in range(1, n):
            for j in range(1, m):
                dp[j] += dp[j - 1]
        return dp[-1]
    
def main():
    m = 7
    n = 3
    a = Solution()
    print(a.uniquePaths(m, n))


if __name__ == '__main__':
    main()
