# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        currA = headA
        currB = headB
        visited = set()
        while currA:
            visited.add(currA)
            currA = currA.next
        while currB:
            if currB in visited:
                return currB
            currB = currB.next
        return            

        