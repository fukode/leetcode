from queue import PriorityQueue
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        if not lists:return
        n = len(lists)
        return self.merge(lists, 0, n-1)
    def merge(self,lists, left, right):
        if left == right:
            return lists[left]
        mid = left + (right - left) // 2
        l1 = self.merge(lists, left, mid)
        l2 = self.merge(lists, mid+1, right)
        return self.mergeTwoLists(l1, l2)
    def mergeTwoLists(self,l1, l2):
        if not l1:return l2
        if not l2:return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

# class Solution(object):
#     def mergeKLists(self, lists):
#         """
#         :type lists: List[ListNode]
#         :rtype: ListNode
#         """
#         amount = len(lists)
#         interval = 1
#         while interval < amount:
#             for i in range(0, amount - interval, interval * 2):
#                 lists[i] = self.merge2Lists(lists[i], lists[i + interval])
#             interval *= 2
#         return lists[0] if amount > 0 else lists
#
#     def merge2Lists(self, l1, l2):
#         head = point = ListNode(0)
#         while l1 and l2:
#             if l1.val <= l2.val:
#                 point.next = l1
#                 l1 = l1.next
#             else:
#                 point.next = l2
#                 l2 = l1
#                 l1 = point.next.next
#             point = point.next
#         if not l1:
#             point.next=l2
#         else:
#             point.next=l1
#         return head.next

def main():
    k = ListNode(0)
    k1 = k
    for i in range(5):
        k1.next = ListNode(i)
        k1 = k1.next

    n = ListNode(0)
    n1 = n
    for i in range(4):
        n1.next = ListNode(i)
        n1 = n1.next

    a = Solution()
    k = a.mergeKLists([k.next, n.next,  ListNode(5)])
    while k:
        print(k.val)
        k = k.next

if __name__ == '__main__':
    main()