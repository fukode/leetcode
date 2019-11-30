class Solution:
    def findMedianSortedArrays(self, A, B):
        m, n = len(A), len(B)
        if m > n:
            m, n, A, B = n, m, B, A

        imin, imax, half_len = 0, m, (m + n + 1) // 2
        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i

            if i < m and B[j-1] > A[i]:
                imin = i + 1
            elif i > 0 and A[i-1] > B[j]:
                imax = i -1
            else:
                if i == 0: max_of_left = B[j-1]
                elif j == 0: max_of_left = A[i-1]
                else: max_of_left = max(A[i-1], B[j-1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m: min_of_right = B[j]
                elif j == n: min_of_right = A[i]
                else: min_of_right = min(B[j], A[i])

                return (max_of_left + min_of_right) / 2

def main():
    nums1 = [1, 3]
    nums2 = [2]
    a = Solution()
    print(a.findMedianSortedArrays(nums1, nums2))
    print(float("-inf"))

if __name__ == '__main__':
    main()