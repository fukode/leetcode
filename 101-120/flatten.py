# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        while root:
            if root.left:
                r = root.left
                while r.right: r = r.right
                r.right = root.right
                root.right = root.left
                root.left = None
            root = root.right
    
def main():
    root = None
    a = Solution()
    print(a.flatten(root))


if __name__ == '__main__':
    main()
