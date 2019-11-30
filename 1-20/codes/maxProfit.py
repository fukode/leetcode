class Solution:
    def maxProfit(self, prices):
        p = 0
        for j in range(1, len(prices)):
            if prices[j] > prices[j - 1]:
                p += (prices[j] - prices[j - 1])

        return p

def main():
    k = [1,2,3,4,5,6,7]
    a = Solution()
    print(a.maxProfit(k))

if __name__ == '__main__':
    main()