# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            Kth = self.getKth(groupPrev, k)
            if not Kth:
                break
            groupNext = Kth.next

            prev, curr = groupNext, groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            temp = groupPrev.next
            groupPrev.next = Kth
            groupPrev = temp

        return dummy.next



    def getKth(self, node, k):
        while node and k > 0:
            node = node.next
            k-=1

        return node