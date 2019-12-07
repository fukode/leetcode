class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        li = relist = ListNode(0)

        while l1 and l2:
            if l1.val <= l2.val:
                relist.next = l1
                l1 = l1.next
            else:
                relist.next = l2
                l2 = l2.next
            relist = relist.next
        if l1:
            relist.next = l1
        else:
            relist.next = l2

        return li.next


def main():
    k = ListNode(0)
    k1 = k
    for i in (-9, 3):
        k1.next = ListNode(i)
        k1 = k1.next

    n = ListNode(0)
    n1 = n
    for i in (5, 7):
        n1.next = ListNode(i)
        n1 = n1.next

    a = Solution()
    k = a.mergeTwoLists(k.next, n.next)
    while k:
        print(k.val)
        k = k.next


if __name__ == '__main__':
    main()