class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        res = 1
        if divisor in {-1, 1}: res = abs(dividend)
        sign = 1 if dividend ^ divisor >= 0 else -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        if dividend < divisor: return 0

        def acountsum(dividend, dor, res):
            if dividend > dor + dor:
                res += acountsum(dividend, dor + dor, res + res)
                return res
            elif dividend > dor:
                return 1 + acountsum(dividend - dor, divisor, 1)
            elif dividend == dor: return 1
            else: return 0

        if res == 1:
            res += acountsum(dividend - divisor, divisor, 1)

        return max(min(res * sign, 2**31 - 1), -2**31)
def main():

    a = Solution()
    print(a.divide(-10, 3))

if __name__ == '__main__':
    main()