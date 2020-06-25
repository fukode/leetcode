# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:
        if not inorder:
            return None
        root = TreeNode(preorder[0])
        i = inorder.index(preorder[0])
        #  preorder inorder
        root.left = self.buildTree(preorder[1: i + 1], inorder[: i])
        root.right = self.buildTree(preorder[i + 1:], inorder[i + 1:])
        # inorder  postorder
        # root.right = self.buildTree(inorder[i+1:], postorder[i:])
        # root.left = self.buildTree(inorder[:i], postorder[:i])
        return root


def main():
    preorder = [1, 2, 3]
    inorder = [2, 3, 1]

    a = Solution()
    print(a.buildTree(preorder, inorder))


if __name__ == '__main__':
    main()
