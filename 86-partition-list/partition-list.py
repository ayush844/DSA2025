# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        dummy_less = ListNode()
        dummy_more = ListNode()

        less = dummy_less
        more = dummy_more

        curr = head

        while curr:
            if curr.val < x:
                less.next = curr
                less = less.next
            else:
                more.next = curr
                more = more.next

            curr = curr.next

        less.next = dummy_more.next
        more.next = None

        return dummy_less.next