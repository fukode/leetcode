class Solution:
    def climbStairs(self, n):
        # import math
        # sum = 1
        # for i in range(1, (n // 2) + 1):
        #     sum += (math.factorial(n - i) / math.factorial(i) / math.factorial(n - i - i))
        # return int(sum)
        dp = [1, 2]
        if n == 1:return 1
        for i in range(n - 2):
            dp[0], dp[1] = dp[1], dp[0] + dp[1]
        return dp[1]


def main():
    n = 10
    a = Solution()
    for i in range(1, n):
        print(a.climbStairs(i))


if __name__ == '__main__':
    main()
