class Solution:
    def generateMatrix(self, n: int):
        # if not n: return []
        # matrix = [[0]*n for _ in range(n)]
        # x = s = 0
        # y = i = 1
        # for s in range(n // 2):
        #     for x in range(s, (n - s) - 1):
        #         matrix[s][x] = i
        #         matrix[x][-s - 1] = i + (n - 2*s) - 1
        #         matrix[-s - 1][-x - 1] = i + 2*((n - 2*s) - 1)
        #         matrix[-x - 1][s] = i + 3*((n - 2*s) - 1)
        #         i += 1
        #     i += ((n - s - y) * 3)
        #     y += 1
        # if n % 2 != 0: matrix[n // 2][n // 2] = n * n
        # return matrix
        r, n = [[n ** 2]], n ** 2
        while n > 1:
            n, r = n - len(r), [[*range(n - len(r), n)]] + [*zip(*r[::-1])]
            print(n, r)
        return r


def main():
    a = Solution()
    s = a.generateMatrix(3)
    for st in s:
        print(st)

if __name__ == '__main__':
    main()