# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, m: int) -> List[List[int]]:
        res = []
        if not root: return res
        s = [(root, [root.val])]
        # def bk(node, s, num):
        #     if not node.left and not node.right and s == 0:
        #         res.append(num)
        #         return
        #     if node.left:
        #         bk(node.left, s - node.left.val, num + [node.left.val])
        #     if node.right:
        #         bk(node.right, s - node.right.val, num + [node.right.val])
        # bk(root, sum - root.val, [root.val])

        while s:
            node, c_sum = s.pop()
            if not node.left and not node.right and sum(c_sum) == m:
                res.append(c_sum)
            if node.left:
                s.append((node.left, c_sum + [node.left.val]))
            if node.right:
                s.append((node.right, c_sum + [node.right.val]))
        return res
    
    
def main():
    root, m = None, 0
    a = Solution()
    print(a.pathSum(root, m))


if __name__ == '__main__':
    main()
