class Solution:
    def nextPermutation(self, nums) -> None:
        n = len(nums)
        k = 1
        for i in range(n - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                k = 0
                x = nums.index(min([x for x in nums[i:] if x > nums[i - 1]]), i)
                nums[x], nums[i - 1] = nums[i - 1], nums[x]
                nums[i:] = sorted(nums[i:])
                break
        if k:
            nums.sort()


def main():

    nums = [5,4,7,5,3,2]
    # x = min([x for x in nums[:] if x > nums[0]])
    # print(x)
    a = Solution()
    print(a.nextPermutation(nums))
    print(nums)


if __name__ == '__main__':
    main()
