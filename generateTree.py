"""
生成二叉树，适用于LEETCODE
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def generateTree(nums):
    if not nums:
        return None
    n = len(nums)
    root = TreeNode(nums.pop(0))
    dic = [root]
    for i, num in enumerate(nums):
        if num is None or num == 'null':
            continue
        tmp = TreeNode(num)
        dic.append(tmp)
        if i % 2 == 0:
            dic[i // 2].left = tmp
        else:
            dic[i // 2].right = tmp
    return root
