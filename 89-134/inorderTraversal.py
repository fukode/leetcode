# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) :
        if not root: return []
        res = []
        s = []
        p = root
        #         def traversal(node):
        #             if node.left:
        #                 traversal(node.left)
        #             res.append(node.val)
        #             if node.right:
        #                 traversal(node.right)
        #         traversal(root)
        while p or s:
            while p:
                s.append(p)
                p = p.left
            p = s.pop()
            res.append(p.val)
            if not p.right and s:
                p = s.pop()
                res.append(p.val)
            p = p.right

        return res
    
    
def main():
    root = TreeNode(0)
    a = Solution()
    print(a.inorderTraversal(root))


if __name__ == '__main__':
    main()
