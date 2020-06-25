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
        cur = root
        n1 = n2 = None
        while cur:
            while cur:
                if cur.left:
                    if not n1:
                        n1 = cur.left
                        n2 = n1
                    else:
                        n1.next = cur.left
                        n1 = n1.next
                if cur.right:
                    if not n1:
                        n1 = cur.right
                        n2 = n1
                    else:
                        n1.next = cur.right
                        n1 = n1.next
                cur = cur.next
            cur = n2
            n1 = None
            n2 = None
        return root
    
def main():
    root = None
    a = Solution()
    print(a.connect_2(root))


if __name__ == '__main__':
    main()
