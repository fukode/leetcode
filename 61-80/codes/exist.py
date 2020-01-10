class Solution:
    def exist(self, board, word):
        n, m = len(board), len(board[0])
        h = [[False] * m for _ in range(n)]

        def bk(x, y, k, h):
            if k == len(word):
                return True
            for i, j in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                tem_x = x + i
                tem_y = y + j
                if 0 <= tem_x < n and 0 <= tem_y < m and\
                        not h[tem_x][tem_y] and word[k] == board[tem_x][tem_y]:
                    h[tem_x][tem_y] = True
                    if bk(tem_x, tem_y, k + 1, h): return True
                    h[tem_x][tem_y] = False

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    h[i][j] = True
                    if bk(i, j, 1, h): return True
                    h[i][j] = False
        return False



def main():
    board =[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
    word = "SEEA"

    a = Solution()
    print(a.exist(board, word))


if __name__ == '__main__':
    main()
