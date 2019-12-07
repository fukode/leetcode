class Solution:
    def removeElement(self, nums, val: int) -> int:
        nums.sort()
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == val:
                nums.pop(i)
            elif nums[i] < val:
                break
        return len(nums)


def main():
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    a = Solution()
    print(a.removeElement(nums, 2))
    print(nums)


if __name__ == '__main__':
    main()
