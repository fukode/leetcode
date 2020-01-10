class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def bk(nums, temp):
            if not nums:
                res.append(temp)
            else:
                for i in range(len(nums)):
                    bk(nums[:i] + nums[i + 1:], temp + [nums[i]])

        bk(nums, [])
        return res
    
    
def main():
    nums = [1,2,3]
    a = Solution()
    print(a.permute(nums))


if __name__ == '__main__':
    main()
