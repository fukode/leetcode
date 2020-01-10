class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        if x == 0: return 0
        if n < 0:
            x, n = 1/x, -n
        temp = x

        def mp(x, temp, n):
            k = 1
            while k + k < n:
                temp *= temp
                k += k
            return x * temp, n - k

        while n > 0:
            x, n = mp(x, temp, n)

        return x/temp

def main():
    x = 2
    n = -2
    a = Solution()
    print(a.myPow(x, n))

if __name__ == '__main__':
    main()