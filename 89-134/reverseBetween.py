class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head, m, n):
        t = head
        x = ListNode(-1)
        x.next, head = head, x
        n -= m
        for i in range(m - 1):
            x = t
            t = t.next
        y, z = t, t.next
        while z and n:
            sceondx = x.next
            y.next = z.next
            x.next = z
            z.next = sceondx
            z = y.next
            n -= 1
        return head.next


def main():
    head = ListNode(0)
    t = head
    for i in range(6):
        t.next = ListNode(i + 1)
        t = t.next
    m = 1
    n = 6
    a = Solution()
    head = a.reverseBetween(head.next, m, n)
    while head:
        print(head.val)
        head = head.next


if __name__ == '__main__':
    main()
