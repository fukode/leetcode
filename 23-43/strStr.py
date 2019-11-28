class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle: return 0

        hlen = len(haystack)
        nlen = len(needle)
        if hlen < nlen: return -1

        i = j = 0
        while i < len(haystack):
            if haystack[i] == needle[j]:
                if hlen - i < nlen: return -1
                for k in range(i + 1, nlen + i):
                    j += 1
                    if haystack[k] != needle[j]:
                        j -= 1
                        break
                if j == nlen - 1: return i
                else: j = 0
            i += 1
        return -1

def main():
    haystack = "mississippi"
    needle = "issip"

    a = Solution()
    print(a.strStr(haystack, needle))

if __name__ == '__main__':
    main()