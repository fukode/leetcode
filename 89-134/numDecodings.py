class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0': return 0
        if len(s) <= 1: return 1
        if s[1] == '0' and s[0] + s[1] > '26': return 0
        dp = [0] * len(s)
        dp[0] = 1
        dp[1] = 2 if ('10' < s[0] + s[1] <= '26' and s[1] != '0') else 1

        for i in range(2, len(s)):
            if s[i] == '0' and (s[i - 1] == '0' or s[i - 1] > '2'):
                return 0
            if s[i] == '0':
                dp[i] = dp[i - 2]
            elif s[i - 1] != '0' and s[i - 1] + s[i] <= '26':
                dp[i] = dp[i - 1] + dp[i - 2]
            else:
                dp[i] = dp[i - 1]

        return dp[-1]
    
def main():
    s = "301"
    a = Solution()
    print(a.numDecodings(s))


if __name__ == '__main__':
    main()
