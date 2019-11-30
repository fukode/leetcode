class Solution:
    def intToRoman(self, num: int) -> str:
        s = ""
        sign = {
            1:'I',
            5:'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M'
        }
        while num > 0:
            if num >= 1000:
                s += sign[1000] * (num // 1000)
                num %= 1000
            elif num >= 500:
                s += (sign[100] + sign[1000]) if num >= 900 else (sign[500] + sign[100] * ((num - 500) // 100))
                num %= 100
            elif num >= 100:
                s += (sign[100] + sign[500]) if num >= 400 else (sign[100] * (num // 100))
                num %= 100
            elif num >= 50:
                s += (sign[10] + sign[100]) if num >= 90 else (sign[50] + sign[10] * ((num - 50) // 10))
                num %= 10
            elif num >= 10:
                s += (sign[10] + sign[50]) if num >= 40 else (sign[10] * (num // 10))
                num %= 10
            elif num >= 5:
                s += (sign[1] + sign[10]) if num >= 9 else (sign[5] + sign[1] * (num - 5))
                num %= 1
            elif num >= 1:
                s += (sign[1] + sign[5]) if num >= 4 else (sign[1] * num)
                num %= 1
        return s
def main():

    a = Solution()
    print(a.intToRoman(60))

if __name__ == '__main__':
    main()