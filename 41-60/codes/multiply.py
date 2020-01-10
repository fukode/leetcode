class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0': return 0

        n1, n2 = len(num1), len(num2)
        rel = 0
        for i in range(n1 - 1, -1, -1):
            ordi = ord(num1[i]) - ord("0")
            for j in range(n2 - 1, -1, -1):
                ordj = ord(num2[j]) - ord("0")
                rel += ordi * pow(10, n1 - i - 1) * ordj * pow(10, n2 - j - 1)
        return str(rel)


def main():
    num1 = "123"
    num2 = "456"
    a = Solution()
    print(a.multiply(num1, num2))


if __name__ == '__main__':
    main()