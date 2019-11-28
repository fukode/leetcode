class Solution:
    def maxProfit(self, prices):
        if not prices: return 0
        n = len(prices)
        dp = [[[0 for _ in range(2)] for i in range(3)] for j in range(n)]
        dp[-1][2][0] = dp[-1][1][0] = 0
        dp[-1][2][1] = dp[-1][1][1] = float('-inf')
        for i in range(n):
            for k in range(3):
                if k == 0:
                    dp[i][0][0] = 0
                    dp[i][0][1] = float('-inf')
                    continue
                dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
        return dp[-1][-1][0]


def main():
    prices = [1,2,4,2,5,7,2,4,9,0]
    a = Solution()
    print(a.maxProfit(prices))


if __name__ == '__main__':
    main()
