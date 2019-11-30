import re
class Solution:
    def myAtoi(self, s: str) -> int:
        return min(max(int(*re.findall('^[\+\-?]?\d+', s.lstrip())), -2**31), 2**31 - 1)


def main():
    s = ""
    # for i in range(1000):
    #  str = str + 'a'

    a = Solution()
    print(a.myAtoi(s))

if __name__ == '__main__':
    main()
