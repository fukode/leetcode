class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def findSize(self, head):
        ptr = head
        c = 0
        while ptr:
            ptr = ptr.next
            c += 1
        return c

    def sortedListToBST(self, head):
        # Get the size of the linked list first
        size = self.findSize(head)
        # Recursively form a BST out of linked list from l --> r

        def convert(l, r):
            nonlocal head
            # Invalid case
            if l > r:
                return None
            mid = (l + r) // 2
            # First step of simulated inorder traversal. Recursively form
            # the left half
            left = convert(l, mid - 1)
            # Once left half is traversed, process the current node
            node = TreeNode(head.val)
            node.left = left
            # Maintain the invariance mentioned in the algorithm
            head = head.next
            # Recurse on the right hand side and form BST out of them
            node.right = convert(mid + 1, r)
            return node
        return convert(0, size - 1)

    
def main():
    num = [-10, -3, 0, 5, 9]
    head = ListNode(num[0])
    temp = head
    for i in range(1, len(num)):
        temp.next = ListNode(num[i])
        temp = temp.next
    a = Solution()
    print(a.sortedListToBST(head))


if __name__ == '__main__':
    main()
