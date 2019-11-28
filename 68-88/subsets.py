class Solution:
    def subsets(self, nums):
        rel = [[]]

        # def bk(j, num):
        #     rel.append(num)
        #     for i in range(j, len(nums)):
        #         bk(i + 1, num + [nums[i]])
        #
        # bk(0, [])
        for i in nums:
            rel = rel + [[i] + num for num in rel]
        return rel


def main():
    nums = [1,2,3,4,5,6,7,8,10,0]
    a = Solution()
    print(a.subsets(nums))


if __name__ == '__main__':
    main()
