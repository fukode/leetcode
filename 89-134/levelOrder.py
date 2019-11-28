# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode):
        if not root: return []
        res = []

        def bk(s):
            if not s:return
            d = []
            num = []
            for i in s:
                num.append(i.val)
                if i.left:
                    d.append(i.left)
                if i.right:
                    d.append(i.right)
            res.append(num)
            bk(d)

        bk([root])
        return res


def main():
    root = TreeNode(2)
    temp = root
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    root = root.right
    root.left = TreeNode(6)
    root.right = TreeNode(20)
    a = Solution()
    print(a.levelOrder(temp))


if __name__ == '__main__':
    main()
