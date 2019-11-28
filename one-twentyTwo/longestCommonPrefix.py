class Solution:
    def longestCommonPrefix(self, strs):
        if "" in strs or not strs: return ""

        longest = min([len(i) for i in strs])
        for i, s in enumerate(strs):
            if i == len(strs) - 1: break
            for j in range(longest):
                if strs[i + 1][j] != s[j]:
                    if j < longest:
                        longest = j

        return strs[0][0:longest] if longest else ''

def main():

    a = Solution()
    print(a.longestCommonPrefix(A))

if __name__ == '__main__':
    main()