# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        self.ans = 0
        def dfs(root, d):
            if not root:
                if d > self.ans:
                    self.ans = d
                return
            dfs(root.left, d + 1)
            dfs(root.right, d + 1)
        dfs(root, 0)
        return self.ans
    
    
def main():
    root = None
    a = Solution()
    print(a.maxDepth(root))


if __name__ == '__main__':
    main()
