# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        #         def bk(l, r):
        #             if not l and not r:
        #                 return True

        #             if l and r:
        #                 return l.val == r.val and bk(l.left, r.right) and bk(l.right, r.left)
        #             else:
        #                 return False
        #         return bk(root.left, root.right)
        s1 = []
        s2 = []
        l = root.left
        r = root.right
        while (l or s1) or (r or s2):
            if (s1 and s2) or (l and r):
                while l or r:
                    if l and r:
                        s1.append(l)
                        s2.append(r)
                        l = l.left
                        r = r.right
                    else:return False
                l = s1.pop()
                r = s2.pop()
                if l.val != r.val or len(s1) != len(s2):
                    return False
                l = l.right
                r = r.left
            else:
                return False
        return True


def main():
    root = TreeNode(1)
    temp = root
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    t = root.right
    root = root.left
    root.left = TreeNode(4)
    root.right = TreeNode(3)
    t.left = TreeNode(3)
    # t.right = TreeNode(4)
    a = Solution()
    print(a.isSymmetric(temp))


if __name__ == '__main__':
    main()
