class Solution:
    def threeSum(self, nums):
        n = len(nums)
        if n < 3: return []
        nums.sort()
        ren = []
        for k in range(n - 2):
            if nums[k] > 0: break
            if k > 0 and nums[k] == nums[k - 1]: continue

            i, j = k + 1, n - 1
            while i < j:
                s = nums[k] + nums[i] + nums[j]
                if s < 0:
                    i += 1
                elif s > 0:
                    j -= 1
                else:
                    ren.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                while i < j and nums[i] == nums[i - 1]: i += 1
                while i < j and nums[j] == nums[j + 1]: j -= 1

        return ren

"""
class Solution:
    def threeSum(self, nums):
        n = len(nums)
        if n < 3: return []

        ren = []
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                temp = [nums[i], nums[j], -(nums[i] + nums[j])]
                temp.sort()
                if -(nums[i] + nums[j]) not in nums or temp in ren:
                    continue
                try:
                    k = nums.index(-(nums[i] + nums[j]), i + 1, j)
                except ValueError:
                    try:
                        k = nums.index(-(nums[i] + nums[j]), j + 1)
                    except ValueError:
                        continue
                if k not in [i, j]:
                    ren.append(temp)
        return ren
"""

def main():

    a = Solution()
    print(a.threeSum([1,0,0,0,-1]))

if __name__ == '__main__':
    main()