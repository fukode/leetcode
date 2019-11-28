class Solution:
    def removeDuplicates(self, nums):
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] == nums[i - 1]:
                nums.pop(i)

        return len(nums)

def main():
    k = [0,0,1,1,1,2,2,3,3,4]
    a = Solution()
    print(a.removeDuplicates(k))

if __name__ == '__main__':
    main()