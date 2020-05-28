class Solution:
    def subsetsWithDup(self, nums):

        res = [[]]
        nums.sort()
        cur = []
        # def bk(j, num):
        #     res.append(num)
        #     for i in range(j, len(nums)):
        #         if i > j and (num + [nums[i]]) == (num + [nums[i - 1]]):
        #             continue
        #         bk(i + 1, num + [nums[i]])
        # bk(0, [])
        # return res
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                cur = [tmp + [nums[i]] for tmp in cur]
            else:
                cur = [tmp + [nums[i]] for tmp in res]
            res += cur
        return res


def main():
    nums = [4,4,4,1,4]
    a = Solution()
    print(a.subsetsWithDup(nums))


if __name__ == '__main__':
    main()
