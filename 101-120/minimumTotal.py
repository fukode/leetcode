class Solution:
    def minimumTotal(self, triangle) -> int:
        #         self.ans = float('inf')

        #         def bk(row, col, num):
        #             if row > len(triangle) - 1:
        #                 self.ans = min(self.ans, num)
        #                 return
        #             bk(row + 1, col, num + triangle[row][col])
        #             bk(row + 1, col + 1, num + triangle[row][col])
        #         bk(0, 0, 0)

        #         return self.ans
        if len(triangle) == 0: return 0
        if len(triangle) == 1: return triangle[0][0]

        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    triangle[i][j] += triangle[i - 1][j]
                elif j == len(triangle[i]) - 1:
                    triangle[i][j] += triangle[i - 1][j - 1]
                else:
                    triangle[i][j] += min(triangle[i - 1][j], triangle[i - 1][j - 1])
        return min(triangle[-1])
    
def main():
    triangle = [[]]
    a = Solution()
    print(a.minimumTotal(triangle))


if __name__ == '__main__':
    main()
