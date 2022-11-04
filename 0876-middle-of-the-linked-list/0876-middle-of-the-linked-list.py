# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #curr=ListNode()
        
        curr=head
        middle=head
        count=0
        while(curr!= None ):
            curr=curr.next
            count+=1
            if(count % 2==0):
                middle=middle.next
        return middle
            
        