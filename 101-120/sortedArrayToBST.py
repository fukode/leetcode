# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):

        if not nums:
            return None
        i = len(nums) // 2
        node = TreeNode(nums[i])
        node.left = self.sortedArrayToBST(nums[:i])
        node.right = self.sortedArrayToBST(nums[i+1:])
        return node

    
def main():
    nums = None
    a = Solution()
    print(a.sortedArrayToBST(nums))


if __name__ == '__main__':
    main()
