class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k == 1: return head
        rep = point = ListNode(0)
        point.next = head
        outflag = True

        def rev(head, end, point):
            temp = end.next
            end.next = end.next.next
            temp.next = head
            head = temp
            point.next = head
            return point.next

        while head:
            for i in range(0, k - 1):
                end = head
                if outflag:
                    for j in range(k - 1):
                        end = end.next
                        if not end:
                            return rep.next
                    outflag = False
                    end = head

                for j in range(i):
                    end = end.next

                head = rev(head, end, point)
                if i == k - 2:
                    head = end.next
                    point = end
                    outflag = True
        return rep.next


def main():
    k = ListNode(0)
    k1 = k
    for i in range(1, 6):
        k1.next = ListNode(i)
        k1 = k1.next
    k1 = k
    a = Solution()
    k = a.reverseKGroup(k.next, 3)
    while k:
        print(k.val)
        k = k.next


if __name__ == '__main__':
    main()
