class Solution:
    def isInterleave(self, s1, s2, s3):
        len_s1 = len(s1)
        len_s2 = len(s2)
        if len_s1 + len_s2 != len(s3): return False

        dp = [[False] * (len_s1 + 1) for _ in range(len_s2 + 1)]
        dp[0][0] = True
        for i in range(len_s1):
            dp[0][i + 1] = (s1[i] == s3[i]) and dp[0][i]
        for j in range(len_s2):
            dp[j + 1][0] = (s2[j] == s3[j])and dp[j][0]

        for i in range(len_s2):
            for j in range(len_s1):
                if dp[i][j + 1]:
                    dp[i + 1][j + 1] = s3[i + j + 1] == s2[i]
                if dp[i + 1][j]:
                    dp[i + 1][j + 1] = s3[i + j + 1] == s1[j] or dp[i + 1][j + 1]
        return dp[-1][-1]


def main():
    # s1 = ""
    # s2 = ""
    # s3 = ""
    # s1 = "ab"
    # s2 = "bc"
    # s3 = "bbac"
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    # s1 = "bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa"
    # s2 = "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab"
    # s3 = "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"
    a = Solution()
    print(a.isInterleave(s1, s2, s3))


if __name__ == '__main__':
    main()
