class Solution:
    def getRow(self, rowIndex: int):
        tmp = []
        for _ in range(rowIndex + 1):
            tmp.insert(0, 1)
            for i in range(1, len(tmp) - 1):
                tmp[i] = tmp[i] + tmp[i+1]
        return tmp
    
def main():
    rowIndex = 5
    a = Solution()
    print(a.getRow(rowIndex))


if __name__ == '__main__':
    main()
