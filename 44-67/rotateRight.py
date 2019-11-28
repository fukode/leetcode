
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head, k):
        n = 0
        if not head or not k: return head
        temp = head
        while temp:
            if not temp.next:
                end = temp
            temp = temp.next
            n += 1

        k = n - (k % n)
        if k == n: return head
        temp = head

        for i in range(k, 0, -1):
            t = temp
            temp = temp.next
            if i - 1 == 0:
                t.next = None
                end.next = head

        return temp
    
    
def main():
    head = ListNode(0)
    k = head
    for i in range(1, 4):
        k.next = ListNode(i)
        k = k.next
    k = 0
    a = Solution()
    head1 = a.rotateRight([], 0)
    while head1:
        print(head1.val)
        head1 = head1.next


if __name__ == '__main__':
    main()
