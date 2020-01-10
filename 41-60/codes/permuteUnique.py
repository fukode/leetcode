class Solution:
    def permuteUnique(self, nums):
        res = []

        def bk(nums, temp):
            if not nums and temp not in res:
                res.append(temp)
            else:
                for i in range(len(nums)):
                    bk(nums[:i] + nums[i + 1:], temp + [nums[i]])
        bk(nums, [])
        return res

def main():

    a = Solution()
    print(a.permuteUnique([1,1,2]))

if __name__ == '__main__':
    main()