class Solution:
    def largestRectangleArea(self, heights):
        t = [-1]
        ans = 0
        for i in range(0, len(heights)):
            while t[-1] != -1 and heights[t[-1]] > heights[i]:
                ans = max(ans, heights[t.pop()] * (i - t[-1] - 1))
            t.append(i)
        while t[-1] != -1:
            ans = max(ans, heights[t.pop()] * (len(heights) - t[-1] - 1))
        return ans


def main():
    heights = [2,1,5,6,2,3]
    a = Solution()
    print(a.largestRectangleArea(heights))


if __name__ == '__main__':
    main()
