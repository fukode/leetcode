class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        te = []
        length = 0
        maxLen = 0
        for i in s:
            if i not in te:
                length += 1
                te.append(i)
                maxLen = max(length, maxLen)
            else:
                te = te[te.index(i) + 1 : ]
                te.append(i)
                length = len(te)
        return maxLen

def main():
    s = "hello world!"
    print(len(s))
    a = Solution()
    print(a.lengthOfLongestSubstring(s))
if __name__ == '__main__':
    main()