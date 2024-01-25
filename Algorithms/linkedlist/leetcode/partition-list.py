# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return None
        d1=ListNode(0)
        d2=ListNode(0)
        ptr1=d1
        ptr2=d2
        
        curr=head
        while curr:
            if curr.val < x:
                ptr1.next=curr
                ptr1=ptr1.next
            else:
                ptr2.next=curr
                ptr2=ptr2.next
            
            curr=curr.next
        ptr1.next=d2.next
        ptr2.next=None

        return d1.next
        

            
        