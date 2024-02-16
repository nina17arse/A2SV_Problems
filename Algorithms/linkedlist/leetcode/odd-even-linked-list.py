# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        leftPtr=head
        evenH=rightPtr=head.next
        
        while rightPtr and rightPtr.next:
            leftPtr.next=leftPtr.next.next
            leftPtr=leftPtr.next
            
            rightPtr.next=rightPtr.next.next
            rightPtr=rightPtr.next

        leftPtr.next=evenH
        return head
            

            
        