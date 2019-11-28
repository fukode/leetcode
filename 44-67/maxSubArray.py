class Solution:
    def maxSubArray(self, nums) -> int:
        n = len(nums)
        if not n: return 0
        if max(nums) <= 0: return max(nums)
        temp = ans = nums[0]
        for i in range(1, n):
            if temp > 0:
                temp += nums[i]
            else:
                temp = nums[i]
            ans = max(ans, temp)

        return ans


def main():
    x = [-2, 1]

    a = Solution()
    print(a.maxSubArray(x))

if __name__ == '__main__':
    main()