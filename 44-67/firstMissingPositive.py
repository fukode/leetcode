class Solution:
    def firstMissingPositive(self, nums) -> int:
        i, n = 0, len(nums)

        while i < n:
            if 0 < nums[i] <= n and nums[i] != i + 1 and nums[nums[i] - 1] != nums[i]:
                temp = nums[i]
                nums[i] = nums[nums[i] - 1]
                nums[temp - 1] = temp
                continue
            i += 1

        for i in range(0, n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1

def main():
    a = Solution()
    print(a.firstMissingPositive([1,1, 4 , 5, 6 ,2]))


if __name__ == '__main__':
    main()