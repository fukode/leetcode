class Solution:
    def combine(self, n, k):
        rel = []
        if n <= 0 or k <= 0 or k > n: return []

        def bk(num, j):
            if len(num) == k:
                rel.append(num)
                return
            for i in range(j, n + 1):
                bk(num + [i], i+1)
        bk([], 1)
        return rel

    
def main():
    n =4
    k = 2
    a = Solution()
    print(a.combine(n, k))


if __name__ == '__main__':
    main()
