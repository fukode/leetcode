
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        h = ListNode(-1)
        h.next = head
        slow = h
        fast = head

        while fast:
            while fast.next and fast.val == fast.next.val:
                fast = fast.next
            if slow.next == fast:
                slow = fast
            else:
                slow.next = fast
            fast = fast.next
        return h.next


def main():
    head = ListNode(0)
    temp = head
    for i in range(1, 6):
        temp.next = ListNode(i)
        temp = temp.next
        if i in (3, 4):
            temp.next = ListNode(i)
            temp = temp.next

    a = Solution()
    head = a.deleteDuplicates(head.next)
    while head:
        print(head.val)
        head = head.next


if __name__ == '__main__':
    main()
