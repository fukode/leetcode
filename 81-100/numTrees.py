"""
给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？
"""


class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1

        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]
        return dp[-1]
    
    
def main():
    n = 3
    a = Solution()
    print(a.numTrees(n))


if __name__ == '__main__':
    main()
