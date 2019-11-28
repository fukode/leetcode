
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        if not head.next: return []
        nNode = ListNode(float("inf"))
        nNode.next = head
        step = 0
        def removen(current, d, step):
            previous = current
            current = current.next
            if current.next:
                cnext, d = removen(current, d, step + 1)

            if d == n:
                if previous.val != float("inf"):
                    previous.next = current.next
                else:
                    current = current.next

            return (current ,d + 1)

        head, k = removen(nNode, 1, 1)

        return head


def main():
    k = ListNode(0)
    k1 = k
    for i in range(1, 5):
        k1.next = ListNode(i)
        k1 = k1.next

    a = Solution()
    k = a.removeNthFromEnd(k.next, 3)
    while k:
        print(k.val)
        k = k.next

if __name__ == '__main__':
    main()