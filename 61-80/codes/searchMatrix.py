class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix: return False
        m, n = len(matrix), len(matrix[0])
        left, right = 0, n * m
        while left < right:
            mid = (left + right) // 2
            num = matrix[mid // n][mid % n]
            if num < target:
                left = mid + 1
            elif num > target:
                right = mid - 1

        return left < n * m and matrix[left // n][left % n] == target

    
def main():
    matrix = [[3]]
    target = 3

    a = Solution()
    print(a.searchMatrix(matrix, target))


if __name__ == '__main__':
    main()
