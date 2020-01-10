class Solution:
    def getPermutation(self, n, k):
        ans = ""
        x = [1, 2, 6, 24, 120, 720, 5040, 40320]
        x = x[:n - 1] if n != 1 else [1]
        nums = [str(i) for i in range(1, n + 1)]
        while k > 0 and nums:
            temp = (k - 1) // x[-1]
            ans += nums.pop(temp)
            k -= ((k - 1) // x[-1]) * x[-1]
            if len(x) > 1:
                x.pop()

        return ans

    
def main():
    n = 4
    k = 6
    a = Solution()
    for k in range(1, 10):
        print(a.getPermutation(1, 1))

if __name__ == '__main__':
    main()
    