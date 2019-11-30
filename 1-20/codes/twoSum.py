class Solution:
    def twoSum_1(self, nums, target):
        h = {}
        for i, n in enumerate(nums):
            if target - n in h:
                return [h[target - n], i]
            h[n] = i


def main():
    nums, target = [2,7,11,15], 9
    a = Solution()
    print(a.twoSum_1(nums, target))


if __name__ == '__main__':
    main()
