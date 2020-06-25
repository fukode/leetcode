class Solution:
    def generate(self, numRows: int):
        res = [[1], [1, 1]]
        if numRows == 0: return []
        if numRows == 1: return res[:1]
        for i in range(2, numRows):
            num = [1]
            for j in range(i - 1):
                num.append(res[-1][j] + res[-1][j + 1])
            res.append(num + [1])
        return res


def main():
    numRows = 5
    a = Solution()
    print(a.generate(numRows))


if __name__ == '__main__':
    main()
