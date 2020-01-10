class Solution:
    def sortColors(self, nums):
        left, right = 0, len(nums) - 1
        i = 0
        while i <= right:
            if nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
            elif nums[i] == 2:
                nums[right], nums[i] = nums[i], nums[right]
                right -= 1
                continue
            i += 1

    
def main():
    nums =[1,2,0]
    a = Solution()
    a.sortColors(nums)
    print(nums)


if __name__ == '__main__':
    main()
