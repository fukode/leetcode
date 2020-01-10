class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head, x):
        left = ListNode(0)
        right = ListNode(0)
        ans = left
        rhead = right
        while head:
            if head.val < x:
                left.next = head
                left = left.next
            else:
                right.next = head
                right = right.next
            head = head.next
        left.next = rhead.next
        right.next = None
        return ans.next

    
def main():
    nums = [1,4,3,2,5,2]
    head = ListNode(0)
    temp = head
    for i in nums:
        temp.next = ListNode(i)
        temp = temp.next
    x = 3
    a = Solution()
    head = a.partition(head.next, x)
    while head:
        print(head.val)
        head = head.next


if __name__ == '__main__':
    main()
