class Solution:
    def maxArea(self, height):
        maxar = i = 0
        j = len(height) - 1

        while i < j:
            maxar = max(min(height[i], height[j]) * (j - i), maxar)
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1

        return maxar

def main():
    k = [1,8,6,2,5,4,8,3,7]
    a = Solution()
    print(a.maxArea(k))

if __name__ == '__main__':
    main()