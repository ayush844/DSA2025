# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        if not head:
            return None

        dummy = ListNode(0, head)
        curr = dummy
        curr = curr.next
        prev = dummy

        while curr and curr.next:
            if curr.next.val == curr.val:
                while curr.next and curr.val == curr.next.val:
                    curr.next = curr.next.next
                prev.next = curr.next
            else:
                prev = prev.next

            curr = curr.next

        return dummy.next