class Solution:
    def totalNQueens(self, n: int) -> int:
        # cbs = []
        rel = [0]
        h = {i: False for i in range(n)}
        lh = {i: False for i in range(2 * n - 1)}
        rh = {i: False for i in range(2 * n - 1)}

        def bvalue(r, c):
            if lh[r + c] or rh[n - c + r - 1]:
                return False
            return True

        def bk(cb):
            cbn = len(cb)
            if cbn == n:
                # cbs.append(cb[:])
                rel[0] += 1
            else:
                for i in range(n):
                    if not h[i] and bvalue(cbn, i):
                        h[i] = lh[cbn + i] = rh[n - i + cbn - 1] = True
                        bk(cb + ['.' * i + 'Q' + '.' * (n - i - 1)])
                        h[i] = lh[cbn + i] = rh[n - i + cbn - 1] = False

        bk([])
        # for i in cbs:
        #     print(i)
        return rel[0]


def main():

    a = Solution()
    cb = a.totalNQueens(4)
    print(cb)

if __name__ == '__main__':
    main()