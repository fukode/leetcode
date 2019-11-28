class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or x % 10 == 0 and x != 0: return False
        ren = 0
        while x > ren:
            ren = ren * 10 + x % 10
            x //= 10
        return x == ren or x == ren // 10
        #return True if x == int(str(x)[:: -1]) else False

def main():
    # s = "PAYPALISHIRING"
    # for i in range(1000):
    #  str = str + 'a'

    a = Solution()
    print(a.isPalindrome(1))

if __name__ == '__main__':
    main()