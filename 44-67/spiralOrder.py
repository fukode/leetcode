class Solution:
    def spiralOrder(self, matrix):
        m = len(matrix)
        if not m: return []
        if m == 1: return matrix[0]
        n = len(matrix[0])
        rel = []
        if n == 1:
            [rel.append(x[0]) for x in matrix]
            return rel
        x = y = 0

        def order(x, y, flag):
            while y != n - i:
                rel.append(matrix[x][y])
                y += flag
                if y < i:
                    break
            if m % 2 == 0 and x == m //2:
                return x, y
            y -= flag
            x += flag
            while x != m - i:
                rel.append(matrix[x][y])
                x += flag
                if x < i + 1:
                    break
            x -= flag
            flag = -flag
            y += flag
            return x, y

        for i in range((min(n, m) + 1) // 2):
            x, y = order(x, y, 1)
            if x != m - 1 and n % 2 != 0 and y == n//2 - 1:break
            x, y = order(x, y, -1)
            if m % 2 != 0 and x == (m // 2):
                rel += matrix[x][y: -y]
                break

        return rel


def main():
    s = [[2,3,4],[5,6,7],[8,9,10],[11,12,13]]
    a = Solution()
    nums = a.spiralOrder(s)
    print(nums)

if __name__ == '__main__':
    main()