class Solution:
    def reverse(self, x: int) -> int:
        x1 = x
        if x1 < 0: x1 = -x

        rex = str(x1)
        rex = list(rex)
        numlen = len(rex)
        for i in range(numlen // 2):
            rex[i], rex[numlen - i - 1] = rex[numlen - i - 1], rex[i]

        rex = "".join(rex)
        rex = int(rex)
        if x < 0: rex = -rex
        if rex > 2147483647 or rex < -2147483648:
            return 0

        return rex


def main():
    #s = "PAYPALISHIRING"
    #for i in range(1000):
      #  str = str + 'a'

    a = Solution()
    print(a.reverse(-123))

if __name__ == '__main__':
    main()