class Solution:
    def convert(self, s: str, numRows: int) -> str:
        string = ""
        slen = len(s)
        if slen <= 1 or numRows == 1 or numRows > slen: return s

        flag = 2 * numRows - 2
        for i in range(numRows):
            n = 0
            while 1:
                if flag * n + i < slen:
                    string += s[flag * n + i]
                    if i != 0 and i != numRows - 1 and (flag * (n + 1) - i) < slen:
                        string += s[flag * (n + 1) - i]
                else: break
                n += 1

        return string

def main():
    s = "PAYPALISHIRING"
    #for i in range(1000):
      #  str = str + 'a'

    a = Solution()
    print(a.convert(s, 3))

if __name__ == '__main__':
    main()