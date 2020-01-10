class Solution:
    def solveNQueens(self, n: int):
        cb = [['.'] * n for _ in range(n)]
        rel = []
        h = {i: False for i in range(n)}

        def bvalue(queens, i):
            if i != 0 and cb[queens - 1][i - 1] == 'Q': return False
            if i != n - 1 and cb[queens - 1][i + 1] == 'Q': return False
            y = i
            while queens != 0 and (y >= 0 or i < n):
                queens -= 1
                y -= 1
                i += 1
                if y >= 0 and cb[queens][y] == 'Q':
                    return False
                if i < n and cb[queens][i] == 'Q':
                    return False
            return True

        def bk(queens, h):
            if queens == n:
                rel.append(["".join(j) for j in cb])
            else:
                for i in range(n):
                    if not h[i] and bvalue(queens, i):
                        cb[queens][i] = 'Q'
                        h[i] = True
                        bk(queens + 1, h)
                        cb[queens][i] = '.'
                        h[i] = False
        bk(0, h)
        return rel
def main():

    a = Solution()
    cb = a.solveNQueens(5)
    print(len(cb))
    for i in cb:
        print(i)

if __name__ == '__main__':
    main()