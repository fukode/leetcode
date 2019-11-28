class Solution:
    def fourSum(self, nums, target: int):
        nums.sort()
        n = len(nums)
        renl = []

        for i in range(n - 3):
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target: break
            if nums[n-1] + nums[n-2] + nums[n-3] + nums[n-4] < target: break
            if (i > 0 and nums[i] == nums[i - 1]) or nums[i] + nums[n-1] + nums[n-2] + nums[n-3] < target: continue

            for j in range(i + 1, n - 2):
                if nums[i] + nums[j + 1] + nums[j + 2] + nums[j] > target: break
                if (j - i > 1 and nums[j] == nums[j - 1]) or nums[j] + nums[n - 1] + nums[n - 2] + nums[
                    i] < target: continue

                x, y = j + 1, n - 1

                while x < y:
                    s = nums[i] + nums[j] + nums[x] + nums[y]

                    if s < target:
                        x += 1
                        while x < y and nums[x] == nums[x - 1]: x += 1
                    elif s > target:
                        y -= 1
                        while x < y and nums[y] == nums[y + 1]: y -= 1
                    else:
                        renl.append([nums[i], nums[j], nums[x], nums[y]])
                        x += 1
                        while x < y and nums[x] == nums[x - 1]: x += 1
                        y -= 1
                        while x < y and nums[y] == nums[y + 1]: y -= 1
        return renl

def main():

    a = Solution()
    print(a.fourSum([-1,0,1,2,-1,-4], -1))

if __name__ == '__main__':
    main()