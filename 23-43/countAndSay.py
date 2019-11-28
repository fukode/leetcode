class Solution:
    def countAndSay(self, n: int) -> str:
        s = ""
        num = "1"
        count = 1
        for i in range(n - 1):
            j = 0
            nlen = len(num)
            while j < nlen:
                if nlen - j > 1 and num[j] == num[j + 1]:
                    count += 1
                else:
                    s = s + str(count) + num[j]
                    count = 1
                j += 1
            num, s = s, ""
        return num


def main():

    a = Solution()
    print(a.countAndSay(5))

if __name__ == '__main__':
    main()