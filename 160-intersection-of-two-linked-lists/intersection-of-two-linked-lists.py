# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        ptA = headA
        ptB = headB

        while ptA != ptB:
            ptA = ptA.next if ptA else headB
            ptB = ptB.next if ptB else headA

        return ptA