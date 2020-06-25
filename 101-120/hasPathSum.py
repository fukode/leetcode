# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:

        #         def bk(node, s):
        #             if not node:
        #                 return False
        #             if not node.left and not node.right:
        #                 return True if s + node.val == sum else False

        #             return bk(node.left, s + node.val) or bk(node.right, s + node.val)
        # return bk(root, 0)
        if not root:
            return False
        s = [(root, sum - root.val), ]
        while s:
            node, c_sum = s.pop()
            if not node.left and not node.right and c_sum == 0:
                return True
            if node.left:
                s.append((node.left, c_sum - node.left.val))
            if node.right:
                s.append((node.right, c_sum - node.right.val))
        return False
    
def main():
    root, sum = None, 0
    a = Solution()
    print(a.hasPathSum(root, sum))


if __name__ == '__main__':
    main()
