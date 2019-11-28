class Solution:
    def searchRange(self, nums, target):
        start, end = 0, len(nums) - 1
        if end == -1: return [-1, -1]
        def finlr(index, mid, flag):# flag = -1 if index = left else flag = 1
            if nums[index] == target: return index
            temp = 0
            while True:
                if nums[index] != target:
                    temp = index
                    index = (index + mid - flag) // 2
                else:
                    if nums[index + flag] == target:
                        index, mid = temp - flag, index
                    else:
                        return index

        while start <= end:
            mid = (start + end) // 2
            if nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                left = finlr(0, mid, -1)
                right = finlr(len(nums) - 1, mid, 1)
                return [left, right]

        return [-1, -1]


def main():

    nums = [0,0,0,1,2,3]
    target = 0
    a = Solution()
    print(a.searchRange(nums, target))

if __name__ == '__main__':
    main()