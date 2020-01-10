class Solution:
    def trap(self, height) -> int:
        i, j = 0, len(height) - 1
        rel = 0
        while i < j:
            while i < j and height[i] <= height[i + 1]: i += 1
            while i < j and height[j] <= height[j - 1]: j -= 1
            if height[i] <= height[j]:
                k = i + 1
                while k <= j and height[k] <= height[i]:
                    rel += (height[i] - height[k])
                    if k == j and height[j] == min(height[i], height[j]):
                        rel -= ((height[j] - height[i]) * (i - j))
                    k += 1
                i = k
            else:
                k = j - 1
                while i <= k and height[j] > height[k]:
                    rel += (height[j] - height[k])
                    if k == i and height[i] == min(height[i], height[j]):
                        rel -= ((height[j] - height[i]) * (j - i))
                    k -= 1
                j = k
        return rel


def main():
    num = [1,1,1,1]
    a = Solution()
    print(a.trap(num))


if __name__ == '__main__':
    main()