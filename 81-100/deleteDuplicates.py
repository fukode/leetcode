# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        if not head or not head.next: return head
        cur = head.next
        pre = head
        while cur:
            if pre.val == cur.val:
                pre.next = cur.next
            else:
                pre = cur
            cur = cur.next
        return head
    
    
def main():
    s = '1->1->2->3->3'.split('->')
    head = ListNode(0)
    temp = head
    for num in s:
        temp.next = ListNode(int(num))
        temp = temp.next
    a = Solution()
    head = a.deleteDuplicates(head.next)
    while head:
        print(head.val)
        head = head.next


if __name__ == '__main__':
    main()
