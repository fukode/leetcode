class Solution:
    def isValidSudoku(self, board) -> bool:
        x = [[] for x in board]
        h = [[] for x in board]
        for i in range(9):
            x[i] = [k[i] for k in board]

        for i in board:
            for j in i:
                if j != '.':
                    if i.count(j) > 1 or x[i.index(j)].count(j) > 1 or \
                            j in h[i.index(j) // 3 + (board.index(i) // 3) * 3]:
                        return False
                    else:
                        h[i.index(j) // 3 + (board.index(i) // 3) * 3].append(j)
        return True


def main():
    board = [
      ["5","3",".",".","7",".",".",".","."],
      ["6",".",".","1","9","5",".",".","."],
      [".","9","8",".",".",".",".","6","."],
      ["8",".",".",".","6",".",".",".","3"],
      ["4",".",".","8",".","3",".",".","1"],
      ["7",".",".",".","2",".",".",".","6"],
      [".","6",".",".",".",".","2","8","."],
      [".",".",".","4","1","9",".",".","5"],
      [".",".",".",".","8",".",".","7","9"]
    ]

    a = Solution()
    print(a.isValidSudoku(board))

if __name__ == '__main__':
    main()