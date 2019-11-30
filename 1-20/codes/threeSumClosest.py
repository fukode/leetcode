class Solution:
    def threeSumClosest(self, nums, target) -> int:
        n = len(nums)
        nums.sort()
        closest = float("inf")
        ren = 0
        for k in range(n - 2):
            if nums[k] >= target: break
            i, j = k + 1, n - 1
            while i < j:
                s = nums[k] + nums[i] + nums[j]

                if s < target:
                    i += 1
                    while i < j and nums[i] == nums[i - 1]: i += 1
                elif s > target:
                    j -= 1
                    while i < j and nums[j] == nums[j + 1]: j -= 1
                else: return target

                if closest > abs(target - s):
                    ren = s
                    closest = min(abs(closest), abs(target - s))

        return ren

def main():

    a = Solution()
    print(a.threeSumClosest([0,1,2], 0))

if __name__ == '__main__':
    main()