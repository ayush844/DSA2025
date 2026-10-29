# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(0, head)

        prev = dummy

        while prev.next and prev.next.next:
            back = prev.next
            front = prev.next.next

            tmp = front.next
            front.next = back
            back.next = tmp
            prev.next = front

            prev = back

        return dummy.next