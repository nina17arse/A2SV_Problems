# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        curr = head
        while curr !=None:
            stack.append(curr.val)
            curr = curr.next
        while head!=None:
            i = stack.pop()
            if head.val !=i:
                return False
            head = head.next
        return True
        