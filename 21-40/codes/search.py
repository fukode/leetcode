class Solution:
    def search(self, nums, target: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            flag = 1 if nums[mid] >= nums[0] else 0
            if nums[mid] < target:
                if not flag and nums[end] < target:
                    end = mid - 1
                else: start = mid + 1
            elif nums[mid] > target:
                if flag and nums[start] > target:
                    start = mid + 1
                else: end = mid - 1
            else:
                return mid
        return -1

        # n = len(nums)
        # if nums[0] > target: return 0
        # if nums[n - 1] < target: return n
        # start, end = 0, n - 1
        # while start < end:
        #     mid = (start + end) // 2
        #     if nums[mid] > target:
        #         end = mid - 1
        #     elif nums[mid] < target:
        #         start = mid + 1
        #     else:
        #         return mid
        # return end if nums[end] > target else end + 1


def main():
    nums = [1,3,5,7,9]
    target = 8
    a = Solution()
    print(a.search(nums, target))


if __name__ == '__main__':
    main()