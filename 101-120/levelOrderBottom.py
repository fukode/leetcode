# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode):
        res = []
        if not root: return res
        #         def bk(node, f):
        #             if f >= len(res):
        #                 res.insert(0, [node.val])
        #             else:
        #                 res[len(res) - f - 1].append(node.val)

        #             if node.left:
        #                 bk(node.left, f + 1)
        #             if node.right:
        #                 bk(node.right, f + 1)
        #         bk(root, 0)
        s = [root]
        while s:
            num = []
            n = len(s)
            for i in range(n):
                if s[0].left: s.append(s[0].left)
                if s[0].right: s.append(s[0].right)
                num.append(s.pop(0).val)
            res.insert(0, num)

        return res


def main():
    root = None
    a = Solution()
    print(a.levelOrderBottom(root))


if __name__ == '__main__':
    main()
