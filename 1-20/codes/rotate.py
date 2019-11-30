class Solution:
    def rotate(self, nums, k: int):

        length = len(nums)
        k = k % length
        idx = count = 0
        while count < length:
            key = nums[idx]
            new_idx = (idx+k) % length
            while new_idx != idx:
                key, nums[new_idx] = nums[new_idx], key
                new_idx = (new_idx+k) % length
                count += 1
            else:
                nums[new_idx] = key
                count += 1
            idx += 1

        return nums

def main():
    nums = [1,2,3,4,5,6]

    a = Solution()
    print(a.rotate(nums, 2))

if __name__ == '__main__':
    main()