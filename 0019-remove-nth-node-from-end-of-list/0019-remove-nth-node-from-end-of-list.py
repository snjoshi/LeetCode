# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp=ListNode(0,head)
        left=temp
        right=head
        
        while n>0 and right is not None:
            right=right.next
            n=n-1
            
        while right is not None:
            right=right.next
            left=left.next
            
        left.next=left.next.next
        return temp.next
            