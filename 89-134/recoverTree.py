class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def recoverTree(self, root):
        # s = []
        # node = None
        # x = y = None
        # while root or s:
        #     while root:
        #         s.append(root)
        #         root = root.left
        #     root = s.pop()
        #     if node and node.val > root.val:
        #         if not x:
        #             x, y = node, root
        #         else:
        #             x.val, root.val = root.val, x.val
        #     node = root
        #     root = root.right
        # if x.val > y.val:
        #     x.val, y.val = y.val, x.val
        f = s = None
        x = None
        while root:
            if root.left is None:
                x = root
                root = root.right
                if not f and x and x.val > root.val:
                    f, s = x.val, root.val
                else:
                    s = root.val
            else:
                pre = root.left
                while pre.right and pre.right != root:
                    pre = pre.right
                if pre.right is None:
                    pre.right = root
                    root = root.left
                else:
                    pre.right = None
                    x = root
                    if not f and x and x.val > root.val:
                        f, s = x.val, root.val
                    else:
                        s = root.val
                    root = root.right

        f.val, s.val = s.val, f.val

    
def main():
    root = TreeNode(3)
    temp = root
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root = root.right
    root.left = TreeNode(2)
    # root.right = TreeNode(2)
    a = Solution()
    print(a.recoverTree(temp))


if __name__ == '__main__':
    main()
