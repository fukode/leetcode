class Solution:
    def setZeroes(self, matrix):
        n, m = len(matrix), len(matrix[0])
        col = -1
        flag = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    if col == -1:
                        col = i
                    matrix[col][j] = 0
                    flag = 1
            if flag and i != col:
                matrix[i] = [0] * m
            flag = 0

        for i in range(m):
            if matrix[col][i]:
                matrix[col][i] = 0
                continue
            for j in range(n):
                matrix[j][i] = 0


def main():
    matrix =[[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]]
    a = Solution()
    a.setZeroes(matrix)
    print(matrix)


if __name__ == '__main__':
    main()
