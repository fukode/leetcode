class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #         if not nums: return 0
        #         num = nums[0]
        #         i, count = 0, 0

        #         while i < len(nums):
        #             if nums[i] == num:
        #                 count += 1
        #                 if count > 2:
        #                     nums.pop(i)
        #                     i -= 1
        #             else:
        #                 count = 1
        #                 num = nums[i]
        #             i += 1

        #         return len(nums)
        n = len(nums)
        if n <= 2: return n
        count = 2

        for i in range(2, n):
            if nums[i] != nums[count - 2]:
                nums[count] = nums[i]
                count += 1

        return count
    
    
def main():
    nums = [0,0,1,1,1,1,2,3,3]
    a = Solution()
    print(a.removeDuplicates(nums))


if __name__ == '__main__':
    main()
