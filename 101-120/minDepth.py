# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        self.m = float('inf')

        def bk(node, d):
            if not node.left and not node.right:
                self.m = min(self.m, d)
                return
            if node.left:
                bk(node.left, d + 1)
            if node.right:
                bk(node.right, d + 1)

        bk(root, 1)
        return self.m
    
def main():
    root = None
    a = Solution()
    print(a.minDepth(root))


if __name__ == '__main__':
    main()
