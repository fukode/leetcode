class Solution:
    def canJump(self, nums) -> bool:
        n = len(nums)
        if 0 not in nums or n == 1:return True
        if nums[0] == 0: return False
        for i in range(n - 1, -1, -1):
            if nums[i] == 0:
                for j in range(i - 1, -1, -1):
                    if nums[j] + j > i or nums[j] + j >= n - 1:
                        break
                    if j == 0:
                        return False
        return True

def main():
    s = [0,1]
    a = Solution()
    nums = a.canJump(s)
    print(nums)

if __name__ == '__main__':
    main()