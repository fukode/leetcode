"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root

        def bk(node):
            if not node.left and not node.right: return
            l = node.left
            r = node.right
            while l and r:
                l.next = r
                l = l.right
                r = r.left
            bk(node.left)
            bk(node.right)

        bk(root)
        return root
    
def main():
    root = None
    a = Solution()
    print(a.connect(root))


if __name__ == '__main__':
    main()
