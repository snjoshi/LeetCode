# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)

        lPrev=dummy
        curr=head
        prev=None
       

        for i in range(left-1):
            lPrev=curr
            curr=curr.next

    
        for i in range(right-left+1):
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node

        lPrev.next.next=curr
        lPrev.next=prev

        return dummy.next
        
        