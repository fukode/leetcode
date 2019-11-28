class Solution:
    def jump(self, nums):
        n = len(nums)
        if n == 1: return 0
        dp = [0] * n
        for i in range(n):
            for j in range(nums[i], 0, -1):
                if i + j >= n -1: return dp[i] + 1
                elif dp[i + j] == 0:
                    dp[i + j] = dp[i] + 1
                else:
                    break

def main():
    num = [5,9,3,2,1,0,2,3,3,1,0,0]
    a = Solution()
    print(a.jump(num))

if __name__ == '__main__':
    main()