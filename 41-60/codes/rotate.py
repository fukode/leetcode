from collections import Counter

class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix) - 1
        for j in range((n + 1) // 2):
            for i in range(len(matrix[0][j: n - j])):
                matrix[0 + j][i + j], matrix[i + j][n - j] = matrix[i + j][n - j], matrix[0 + j][i + j]
                matrix[0 + j][i + j], matrix[n - j][n - i - j] = matrix[n - j][n - i - j], matrix[0 + j][i + j]
                matrix[0 + j][i + j], matrix[n - i - j][0 + j] = matrix[n - i - j][0 + j], matrix[0 + j][i + j]
            """
                0.
                [0][n]
                [n][n]
                [n][0]
               1.
               [1][n]
               [n][n - 1]
               [n - 1][0]
               2
               [2][n]
               [n][n - 2]
               [n - 2][0]
            """


def main():
    # matrix = [
    #     [5, 1, 9, 11],
    #     [2, 4, 8, 10],
    #     [13, 3, 6, 7],
    #     [15, 14, 12, 16]
    # ]
    matrix =[
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    a = Solution()
    for i in matrix:
        print(i)

if __name__ == '__main__':
    main()