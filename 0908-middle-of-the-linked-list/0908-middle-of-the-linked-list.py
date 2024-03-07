"""
2 point while arrive at none
Add dummy at first
1st: move 2 -> 
2nd: move 1 -> 

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p1,p2=head,head
        while p1 is not None and p1.next is not None:
            p1=p1.next.next
            p2=p2.next
        return p2