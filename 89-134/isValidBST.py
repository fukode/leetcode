# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # s = []

        # while root:
        #     if root.right and root.right.val <= root.val:return False
        #
        #     while root.left:
        #         if root.right:
        #             if root.val < root.right.val:
        #                 s.append(root.right)
        #             else:
        #                 return False
        #         if root.val > root.left.val:
        #             root = root.left
        #         else:
        #             return False
        #     if s:
        #         root = s.pop().left
        #     else:
        #         root = root.left
        # return True

        def bk(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True

            val = node.val
            if val <= lower or val >= upper:
                return False
            if not bk(node.right, val, upper):
                return False
            if not bk(node.left, lower, val):
                return False
            return True

        return bk(root)

        s = [(root, float('-inf'), float('inf'))]
        while s:
            root, lower, upper = s.pop()
            if not root:
                continue
            val = root.val

            if val <= lower or val >= upper:
                return False
            s.append((root.left, lower, val))
            s.append((root.right, val, upper))
        return True


def main():

    root = TreeNode(2)
    temp = root
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    root = root.right
    root.left = TreeNode(6)
    root.right = TreeNode(20)

    a = Solution()
    print(a.isValidBST(temp))


if __name__ == '__main__':
    main()
