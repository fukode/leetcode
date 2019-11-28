class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:

        if head and head.next:
            n = head.next
            head.next = self.swapPairs(n.next)
            n.next = head

            return n
        else: return head

def main():
    k = ListNode(0)
    k1 = k
    for i in range(5):
        k1.next = ListNode(i)
        k1 = k1.next
    k1 = k

    a = Solution()
    k = a.swapPairs(k.next)
    while k:
        print(k.val)
        k = k.next

if __name__ == '__main__':
    main()
