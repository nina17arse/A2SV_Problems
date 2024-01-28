# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # sol=None
        # index=0
        # while head != None:
        #     next_node=head.next
        #     head.next=sol
        #     sol=head
        #     head=next_node
        # curr=head
        # while curr and  index<n-1:
        #     curr=curr.next
        #     index+=1

        # curr.next=curr.next.next
        # while head != None:
        #     next_node=head.next
        #     head.next=sol
        #     sol=head
        #     head=next_node
        # return head
        fast = head
        slow = head
        for i in range(n):
            fast = fast.next
            
        if not fast:
            return head.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return head

        
        