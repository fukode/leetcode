# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.flag = True

        def bk(node):
            if not node:
                return 0
            left = bk(node.left) + 1
            right = bk(node.right) + 1

            if abs(right - left) > 1:
                self.flag = False
            return max(left, right)

        bk(root)
        return self.flag


def main():
    root = None
    a = Solution()
    print(a.isBalanced(root))


if __name__ == '__main__':
    main()
