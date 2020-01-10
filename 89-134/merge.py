class Solution:
    def merge(self, nums1, m, nums2, n):
        for i in range(len(nums1) - 1, -1, -1):
            if m > 0 and n > 0:
                if nums1[m - 1] >= nums2[n - 1]:
                    nums1[i] = nums1[m - 1]
                    m -= 1
                else:
                    nums1[i] = nums2[n - 1]
                    n -= 1
        if n >= 0:
            nums1[0: n] = nums2[0: n]


def main():
    nums1 = [2,0,0]
    m = 1
    nums2 = [1,2]
    n = 2
    a = Solution()
    a.merge(nums1, m, nums2, n)
    print(nums1)


if __name__ == '__main__':
    main()
