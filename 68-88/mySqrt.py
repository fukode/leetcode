class Solution:
    def mySqrt(self, x):
        if x == 0: return x
        if x < 4: return 1

        ans = x
        while ans ** 2 > x:
            ans = (ans + x / ans) // 2

        return int(ans)


def main():
    x = 1241022903
    a = Solution()
    print(a.mySqrt(x))


if __name__ == '__main__':
    main()
