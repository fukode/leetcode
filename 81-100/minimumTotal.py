class Solution:
    def minimumTotal(self, triangle) -> int:
        ans = 0
        index = 0
        for i in range(len(triangle)):
            ans += triangle[i][index]
            if i != len(triangle) - 1:
                index = index if triangle[i + 1][index] < triangle[i + 1][index + 1] else index + 1
        return ans
    
def main():
    triangle = [[2],[3,4],[6,7,5],[4,1,8,3]]
    a = Solution()
    print(a.minimumTotal(triangle))


if __name__ == '__main__':
    main()
