# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode):
        if not root: return []
        res = []
        node = [root]
        flag = 1
        while node:
            num = []
            for i in range(len(node)):
                if node[0].left:
                    node.append(node[0].left)
                if node[0].right:
                    node.append(node[0].right)
                num.append(node.pop(0).val)
            if flag % 2 == 0:
                num = num[::-1]
            res.append(num)
            flag += 1
        return res
    
def main():
    root = None
    a = Solution()
    print(a.zigzagLevelOrder(root))


if __name__ == '__main__':
    main()
