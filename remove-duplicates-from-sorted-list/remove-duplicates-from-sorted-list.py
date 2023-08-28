# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first=head
        
        while first!=None and first.next!=None:
            if first.val == first.next.val:
                first.next=first.next.next
            else:
                first=first.next
                
        return head
            
        