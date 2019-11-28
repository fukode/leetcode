import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(re.compile('[^a-zA-Z0-9]'), "", s).lower()
        return s[::-1] == s


def main():
    s = "A man, a plan, a canal: Panama"
    a = Solution()
    print(a.isPalindrome(s))


if __name__ == '__main__':
    main()
