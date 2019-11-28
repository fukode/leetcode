class Solution:
    def solve_130(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        # if not board: return board
        # n, m = len(board), len(board[0])
        # hs = {(i, j): False for i in range(n) for j in range(m)}
        # # print(hs)
        #
        # def bfs(i, j):
        #     if i > 0 and board[i - 1][j] == 'O' and not hs[i - 1, j]:
        #         hs[i - 1, j] = True
        #         bfs(i - 1, j)
        #     if i < n - 1 and board[i + 1][j] == 'O' and not hs[i + 1, j]:
        #         hs[i + 1, j] = True
        #         bfs(i + 1, j)
        #     if j > 0 and board[i][j - 1] == 'O' and not hs[i, j - 1]:
        #         hs[i, j - 1] = True
        #         bfs(i, j - 1)
        #     if j < m - 1 and board[i][j + 1] == 'O' and not hs[i, j + 1]:
        #         hs[i, j + 1] = True
        #         bfs(i, j + 1)
        #
        # for i in (0, n - 1):
        #     for j in range(m):
        #         if board[i][j] == 'O':
        #             bfs(i, j)
        # for i in (0, m - 1):
        #     for k in range(1, n - 1):
        #         if board[k][i] == 'O':
        #             bfs(k, i)
        #
        # for i in range(1, n - 1):
        #     for j in range(1, m - 1):
        #         if board[i][j] == 'O' and not hs[i, j]:
        #             board[i][j] = 'X'
        f = {}

        def find(x):
            f.setdefault(x, x)
            if f[x] != x:
                f[x] = find(f[x])
            return f[x]

        def union(x, y):
            f[find(y)] = find(x)

        if not board or not board[0]:
            return
        row = len(board)
        col = len(board[0])
        dummy = row * col
        for i in range(row):
            for j in range(col):
                if board[i][j] == "O":
                    if i == 0 or i == row - 1 or j == 0 or j == col - 1:
                        union(i * col + j, dummy)
                    else:
                        for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            if board[i + x][j + y] == "O":
                                union(i * col + j, (i + x) * col + (j + y))
        for i in range(row):
            for j in range(col):
                if find(dummy) == find(i * col + j):
                    board[i][j] = "O"


def main():
    board = [["X","O","X","X"],["O","X","O","X"],["X","O","X","O"],["O","X","O","X"],["X","O","X","O"],["O","X","O","X"]]
    Solution().solve_130(board)
    print(board)


if __name__ == '__main__':
    main()
