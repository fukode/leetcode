class Solution:
    def addBinary(self, a: str, b: str):
        n, m = len(a) - 1, len(b) - 1
        if n < m: n, m, a, b = m, n, b, a
        a = list(map(int, a))
        b = list(map(int, b))
        flag = 0
        while m >= 0:
            if flag:
                if a[n]:
                    a[n] = 0
                else:
                    a[n] = 1
                    flag = 0
            if a[n] == b[m] == 1:
                flag = 1
                a[n] = 0
            elif a[n] or b[m]:
                a[n] = 1
            m -= 1
            n -= 1

        if flag and n == m:
            a.insert(0, 1)
        elif flag:
            for i in range(n, -1, -1):
                if a[i]:
                    a[i] = 0
                else:
                    a[i] = 1
                    break
            if a[0] == 0:
                a.insert(0, 1)
        return "".join(list(map(str, a)))



def main():
    s = "1010"
    b = "1011"
    a = Solution()
    print(a.addBinary(s, b))


if __name__ == '__main__':
    main()
